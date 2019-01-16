from django.db import models
from bloguser.models import UserInfo
# Create your models here.

class Album(models.Model):
    author = models.ForeignKey(UserInfo)
    title = models.CharField(max_length=150, verbose_name='标题')
    description = models.TextField(max_length=500, verbose_name='描述信息')
    img = models.ImageField(upload_to='photos/', default='photos/no-img.jpg')
    # img = models.FileField(upload_to='photos/')
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # def __str__(self):
    #     """
    #     返回Album对象的str表示形式
    #     """
    #     return self.title


class Photo(models.Model):
    """
    用户照片
    """
    title = models.CharField(max_length=150,null=True)
    user= models.ForeignKey(UserInfo)
    question = models.ForeignKey(Album)
    img = models.ImageField(upload_to='photos/', default='photos/no-img.jpg')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    #
    # def __str__(self):
    #     """
    #     返回Photo对象的str表示形式
    #     """
    #     return  self.title

class Blog(models.Model):
    author = models.ForeignKey(UserInfo)
    title = models.CharField(max_length=150, verbose_name='标题')
    maincontent = models.CharField(max_length=150, verbose_name='摘要')
    description = models.TextField(max_length=500, verbose_name='描述信息')
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')