from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

class Type(models.TextChoices):
    Positve = 'ADD' ,"POSITIVE"
    Negative = 'SUBTRACT',"SUBTRACT"





class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=CASCADE , null = True)
    income = models.FloatField(null = True)
    income_category = models.CharField(max_length=100 , null = True, blank = True)
    created_date = models.DateField(auto_now_add = True , blank = True , null = True)
    expenses = models.FloatField(default=0) 
    balance = models.FloatField(null = True , blank = True)
    currency_type = models.CharField(max_length=100,default='EUR')
    curr_value = models.FloatField()

    def __str__(self) :
        return str(self.user)

class Add_Excel(models.Model):
    income = models.FloatField()
    income_category = models.CharField(max_length=100 , null = True, blank = True)
    expenses   =  models.FloatField(default=0) 
    user = models.CharField(max_length=100 , null=True , blank= True)

    def __str__(self):
        return str(self.income_category)



class Tracker(models.Model):
    user = models.ForeignKey(Profile , on_delete=CASCADE)
    category  = models.CharField(max_length=100 , null = True , blank = True )
    name = models.CharField(max_length=75)
    amount = models.FloatField(null= True , blank = True)
    expence_type = models.CharField(max_length=100 , choices=Type.choices , null=True , blank=True)


    def __str__(self):
        return self.name
    

