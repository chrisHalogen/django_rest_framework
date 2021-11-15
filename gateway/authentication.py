import jwt
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework.authentication import BaseAuthentication
from user.models import Person

class Authentication(BaseAuthentication):

    def authenticate(self,request):
        data = self.validate_request(request.headers)

        if not data:
            return None,None
        
        return self.getUser(data["user_id"]),None
    
    def getUser(self,user_id):
        try:
            user = Person.objects.get(id=user_id)
            return user
        except Exception:
            return None


    def validate_request(self,headers):
        authorization = headers.get("Authorization",None)
        
        if not authorization:
            return None
        
        token = headers["Authorization"][7:]
        
        decodedData = Authentication.verifyToken(token)

        if not decodedData:
            return None
        
        return decodedData



    def verifyToken(token):
        try:
            decodedData = jwt.decode(
                token,settings.SECRET_KEY, algorithms=['HS256']
            )
        except Exception:
            return None
        
        expiryDate = decodedData['exp']

        if datetime.now().timestamp() > expiryDate:
            return None
        
        return decodedData