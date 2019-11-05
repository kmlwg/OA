from django.db import models
from datetime import datetime


class User(models.Model):
	login = models.CharField(max_length=10)
	password = models.CharField(max_length=20)
	mail = models.EmailField()


class Company(models.Model):
	login = models.CharField(max_length=10)
	password = models.CharField(max_length=20)
	mail = models.EmailField()


class Profile(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=30)
	telephone = models.CharField(max_length=30)
	opening_hours = models.CharField(max_length=30)
	sales = models.CharField(max_length=30)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Forum(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	text = models.CharField(max_length=250)
	date = models.DateTimeField(default=datetime.now)
