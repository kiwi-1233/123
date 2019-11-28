# -*- coding: utf-8 -*-
"""
*************************************************
 Create Time:  2019/11/28 21:56
 Project Name: django项目
 File Name:    permission_init
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
from django.conf import settings
def permission_init(request,user_obj):
    permission = user_obj.role.filter (permission__url__isnull=False).values (
        'permission__url' ,
        'permission__icon' ,
        'permission__is_menu' ,
        'permission__tittle'
    ).distinct ()

    permission_list = []
    # 菜单列表
    menu_list = []
    # menu_list = [{'tittle':'','url':'','icon':''}]
    for i in permission :  # 获取作为菜单的权限url
        permission_list.append ({ 'url' : i['permission__url'] })
        if i['permission__is_menu'] :
            menu_list.append ({
                'tittle' : i['permission__tittle'] ,
                'url' : i['permission__url'] ,
                'icon' : i['permission__icon'] ,
            })

    request.session['is_ok'] = True
    # 将部分session在settings中进行配置避免写死
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_list

