from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
import datetime


# Create your models here.
class User(AbstractUser):
    username = None
    mobile = models.CharField(max_length=12,unique=True)
    balance = models.IntegerField(default=0)
    image = models.ImageField(upload_to="alluser/img",default='img/usera.jpg')
    mailing_address = models.CharField(max_length=200, blank=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'mobile'

    def __str__(self):
        return self.mobile

class Uhistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ufrom = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    dmoney = models.IntegerField(default=0)
    histype = models.CharField(max_length=100,default=0)
    
    def __str__(self):
        return self.user.mobile

class loanapply(models.Model):
    name = models.CharField(max_length=100,default=0) 
    lmobile = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    tloan = models.CharField(max_length=100,default=0)

    def __str__(self):
        return self.name    