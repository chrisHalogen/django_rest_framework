from django.shortcuts import render
from .models import JWT
from user.models import Person
from datetime import datetime, timedelta
import jwt
from django.conf import settings
import random, string
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .authentication import Authentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def getRandomString(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits,k=length))

def get_access_token(payload):
    return jwt.encode(
        {'exp':datetime.now() + timedelta(minutes=5),**payload},
        settings.SECRET_KEY,
        algorithm='HS256'
    )

def get_refresh_token():
    return jwt.encode(
        {'exp':datetime.now() + timedelta(days=10),'date':getRandomString(20)},
        settings.SECRET_KEY,
        algorithm='HS256'
    )

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)

        user = authenticate(
            username = serializer.validated_data['email'],
            password = serializer.validated_data['password']
        )

        if not user:
            return Response({
                'error':'Invalid Email or Password',
            }, status='400')
        
        if JWT.objects.filter(user_id=user):
            JWT.objects.filter(user_id=user).delete()
        
        access = get_access_token({'user_id':user.id})
        refresh = get_refresh_token()

        JWT.objects.create(
            user_id = user, access_token = access, refresh_token = refresh
        )

        return Response({
            'access':access, 'refresh':refresh
        })


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)

        Person.objects._create_user(**serializer.validated_data)

        return Response(
            {'message':"User Created Successfully"},
            status='200'
        )




class RefreshView(APIView):
    serializer_class = RefreshSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)

        try:
            active_JWT = JWT.objects.get(refresh_token=serializer.validated_data['refresh'])
        
        except JWT.DoesNotExist:
            return Response(
                {'message':'Token not found'}, status='400'
            )

        if not Authentication.verifyToken(serializer.validated_data['refresh']):
            return Response({'message':'Token is Invalid or Expired'},status='400')

        access = get_access_token({'user_id':active_JWT.user_id.id})
        refresh = get_refresh_token()

        active_JWT.access_token = access
        active_JWT.refresh_token = refresh

        active_JWT.save()

        return Response({
            'access':access, 'refresh':refresh
        })


class GetSecuredInfo(APIView):

    # authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        # print(request.user)
        return Response({
            'message':'Secured Information for Logged In users alone'
        })


class TestException(APIView):

    def get(self,request):
        try:
            a = 24 / 0

        except Exception as e:
            raise Exception("You Can't divide by zero")


        return Response({
            'message':'Secured Information for Logged In users alone'
        })