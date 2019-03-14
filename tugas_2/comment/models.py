from django.db import models

# Create your models here.
class Comment(models.Model):
	comment = models.CharField(max_length=50)
	userName = models.CharField(max_length=50)
	createdBy = models.CharField(max_length=50)
	createdAt = models.DateTimeField()
	updatedAt = models.DateTimeField()