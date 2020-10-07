from django.db import models

# Create your models here.

class UserModel(models.Model):
	name = models.CharField(max_length=250)
	mobile = models.IntegerField()
	password = models.CharField(max_length=10)
	def __str__(self):
		return self.name
