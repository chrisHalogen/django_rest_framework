from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Blog(models.Model):
	name = models.CharField(max_length=255)
	content = models.TextField()
	author = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True);updated = models.DateTimeField(auto_now=True)

class Dog(models.Model):
	url = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.url
	