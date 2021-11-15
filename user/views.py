from rest_framework.viewsets import ModelViewSet
from .serializers import Person, UserSerializer, UserProfile, UserProfileSerializer

class CustomUserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = Person.objects.all()


class ProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()