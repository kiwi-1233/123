# -*- coding: utf-8 -*-
"""
*************************************************
 Create Time:  2019/11/27 18:09
 Project Name: django项目
 File Name:    middleware
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
from django.shortcuts import redirect,render,HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import re


class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        url = request.path_info
        for i in settings.WHITE_LIST:
            if re.match(i,url):
                return

        is_ok = request.session.get('is_ok')
        if not is_ok:
            return redirect('/login/')

        for i in settings.PASS_LIST:
            if re.match(i,url):
                return

        permission = request.session.get(settings.PERMISSION_SESSION_KEY)
        print(permission)
        if permission:
            for i in  permission:
                if re.match(r'^{}$'.format(i['url']),url):
                    return
        return HttpResponse('无访问权限')



