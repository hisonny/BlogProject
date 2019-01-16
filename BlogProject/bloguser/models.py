from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11,null=True,blank=True,unique=True,verbose_name='手机号')
    age = models.IntegerField(null=True,blank=True,unique=True,verbose_name='年龄')