from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150,unique=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category,on_delete =models.CASCADE)
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length=150,unique =True)
	image = models.FileField(upload_to='media')
	description = models.TextField()
	price = models.DecimalField(max_digits=10,decimal_places=2)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
