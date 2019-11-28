# -*- coding: utf-8 -*-
"""
*************************************************
 Create Time:  2019/11/28 20:45
 Project Name: django项目
 File Name:    my_tags
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
from django.template import Library
from django.conf import settings
import re
register = Library()

@register.inclusion_tag('rbac_menu.html')
def menu(request):
    url = request.path_info

    menu_list = request.session.get(settings.MENU_SESSION_KEY)

    for i in menu_list:
        if re.search(r'{}'.format(i['url'].split('/')[1]),url):
            i['class'] = 'active'
    return {'menu_list':menu_list}

