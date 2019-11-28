# -*- coding: utf-8 -*-
"""
*************************************************
 Create Time:  2019/11/27 18:24
 Project Name: django项目
 File Name:    account
 Author:       w1887
*************************************************
# code is far away from bugs with the god animal
 protecting.I love animals. They taste delicious.
   ┏┓      ┏┓
  ┏┛┻━━━━━━┛┻┓
  ┃    ☃     ┃
  ┃ ┳┛   ┗┳  ┃
  ┃    ┻     ┃
  ┗━┓      ┏━┛
    ┃      ┗━━━┓
    ┃  神兽保佑   ┣┓
    ┃   永无BUG！  ┏┛
    ┗┓┓┏━━┳┓┏┛
     ┃┫┫  ┃┫┫
     ┗┻┛  ┗┻┛ 
"""
from django.shortcuts import render,redirect,HttpResponse
from rbac.service.permission_init import permission_init
from django.conf import settings
from rbac import models
import copy

def login(request) :
    error = ''
    if request.method == 'POST' :
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user_obj = models.Users.objects.filter (username=username , password=password).first()
        if not user_obj :

            error = '账户或密码错误'
            return render (request,'login.html',{ 'error' : error })
       #登陆成功后的权限信息初始化
        permission_init(request,user_obj)
        return redirect('/index/')
    return render (request , 'login.html')

def index(request):
    return render(request,'index.html')