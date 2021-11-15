from rest_framework import serializers
from .models import Person, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('email','name','created_at','updated_at')

class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('__all__')