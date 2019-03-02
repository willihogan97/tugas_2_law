from django.db import models

# Create your models here.
class User(models.Model):
	userId = models.CharField(max_length=50)
	displayName = models.CharField(max_length=50)