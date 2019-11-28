'''
@Author: kiwi
@Date: 2019-11-27 12:28:55
@LastEditors: kiwi
@LastEditTime: 2019-11-28 08:36:52
@Description: 描述
'''
from django.db import models


# Create your models here.
class Users (models.Model) :
    """Model definition for Users."""

    username = models.CharField ('用户名' , max_length=32)
    password = models.CharField ('密码' , max_length=32)
    role = models.ManyToManyField (verbose_name='具有的所有角色' , to="Role" , blank=True)

    class Meta :
        """Meta definition for Users."""

        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self) :
        """Unicode representation of Users."""
        return self.username


class Role (models.Model) :
    rolename = models.CharField ('角色名' , max_length=32)
    permission = models.ManyToManyField (verbose_name='具有的所有权限' , to='Permission' , blank=True)

    class Meta :
        verbose_name = '角色表'
        verbose_name_plural = verbose_name

    def __str__(self) :
        return self.rolename


class Permission (models.Model) :
    tittle = models.CharField ('权限名' , max_length=32)
    url = models.CharField ('带正则的url' , max_length=50)
    is_menu = models.BooleanField(default=False,verbose_name='是否为菜单') # 判断是否为菜单的字段
    icon = models.CharField(max_length=64,verbose_name='图标',blank=True,null=True) #存储图标的字段
    class Meta :
        verbose_name = '权限表'
        verbose_name_plural = verbose_name

    def __str__(self) :
        
        return self.tittle
