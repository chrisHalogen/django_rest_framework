from django.contrib import admin
from .models import Person, UserProfile
# Register your models here.

admin.site.register(Person)
admin.site.register(UserProfile)