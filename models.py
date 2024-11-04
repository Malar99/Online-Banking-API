from django.db import models
class deposit(models.Model):
	name=models.CharField(max_length=65)
	amount=models.IntegerField(max_length=64)
	accountId=models.IntegerField(max_length=64)
	date=models.DateField(max_length=64)

class createaccount(models.Model):
	aname=models.CharField(max_length=64)
	anumber=models.IntegerField(max_length=64)
	age=models.IntegerField(max_length=64)
	adate=models.DateField(max_length=64)