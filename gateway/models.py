from django.db import models
from user.models import Person

# Create your models here.

class JWT(models.Model):
    user_id = models.OneToOneField(Person, related_name='logged_in_user', on_delete=models.CASCADE)
    access_token = models.TextField()
    refresh_token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)