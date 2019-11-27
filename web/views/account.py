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
from rbac import models


def login(request) :
    error = ''
    if request.method == 'POST' :
        print(1)
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user_obj = models.Users.objects.filter (username=username , password=password).first()
        if not user_obj :
            print(2)
            error = '账户或密码错误'
            return render (request,'login.html',{ 'error' : error })
        permission =  user_obj.role.filter(permission__url__isnull=False).values('permission__url')
        print(permission)
        request.session['is_ok'] = True
        request.session['url'] = list(permission)
        return redirect('/index/')
    return render (request , 'login.html')

def index(request):
    return render(request,'index.html')