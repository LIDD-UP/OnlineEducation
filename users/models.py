from django.db import models
# 由于django自带的user不满足我们的需求，需要导入原始的AbstractUser然后进行继承添加新的字段；
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    # nick_name
    nich_name = models.CharField(max_length=50,verbose_name="昵称",default='')
    # 性别 gender 使用charFiled 下的choice
    gender = models.CharField(choices=(('male','男'),('female','女')),blank=True,default='male',max_length=5,verbose_name='性别')
    # 生日
    birthday = models.DateField(verbose_name='生日',blank=True)
    # address地址
    address = models.CharField(max_length=100,default='',verbose_name='地址',blank=True)
    # mobiles 手机号（11位）
    mobiles = models.CharField(max_length=11,null=True,verbose_name='手机')
    # 头像文件字段Imagefield需要看官方文档看具体的用法；
    image = models.ImageField(upload_to='image/%Y/%m',verbose_name='头像',max_length=100,default='image/default.png')
    # Meta信息
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    # 重要方法的重载，如果 不重载，再打印usrprofile的实例的时候会出错；
    # python 2中是重载unicode方法；
    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    # code
    # email
    # send_type 发送类型：包括注册和找回密码
    
