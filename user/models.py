from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):

	def _create_user(self,email,password, **extra_fields):

		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_active',True)
		
		if extra_fields.setdefault('is_staff') is not True:
			raise ValueError('user must be staff')
		if extra_fields.setdefault('is_active') is not True:
			raise ValueError('User Must be active')

		if not email:
			raise ValueError('Email is Required')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self,email,password, **extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser',True)
		extra_fields.setdefault('is_active',True)
		extra_fields.setdefault('name','admin')

		if extra_fields.setdefault('is_staff') is not True:
			raise ValueError('Superuser must be staff')
		if extra_fields.setdefault('is_superuser') is not True:
			raise ValueError('Superuser must be superuser')

		return self._create_user(email,password, **extra_fields)

class Person(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=225)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_staff = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	objects = CustomUserManager()
	
	class Meta:
		verbose_name_plural = 'People on the Website'

	def __str__(self):
		return self.email


class UserProfile(models.Model):
	user = models.OneToOneField(Person,on_delete=models.CASCADE, related_name='user_profile')
	profile_picture = models.ImageField()
	dob = models.DateField()

	def __str__(self):
		return self.user.email
