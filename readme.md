# 权限组件第一版
![SharedScreenshot1](C:%5CUsers%5Cw1887%5Cdjango%E9%A1%B9%E7%9B%AE%5Cassets%5CSharedScreenshot1.jpg)



## 1.建立表关系

```python
from django.db import models


# Create your models here.
class Users (models.Model) :
    #用户表
    username = models.CharField ('用户名' , max_length=32)
    password = models.CharField ('密码' , max_length=32)
    #角色多对多关联角色表
    role = models.ManyToManyField (verbose_name='具有的所有角色' , to="Role" , blank=True)

    class Meta :
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self) :
        
        return self.username


class Role (models.Model) :
    """
    角色表
    权限字段多对多关联权限表
    """
    rolename = models.CharField ('角色名' , max_length=32)
    permission = models.ManyToManyField (verbose_name='具有的所有权限' , to='Permission' , blank=True)

    class Meta :
        verbose_name = '角色表'
        verbose_name_plural = verbose_name

    def __str__(self) :
        return self.rolename


class Permission (models.Model) :
    """
    权限表
    """
    tittle = models.CharField ('权限名' , max_length=32)
    url = models.CharField ('带正则的url' , max_length=50)

    class Meta :
        verbose_name = '权限表'
        verbose_name_plural = verbose_name

    def __str__(self) :
        return self.tittle

```

## 2.rbac app 中的admin进行注册：
```python
from django.contrib import admin
from rbac import models
# Register your models here.

admin.site.register(models.Users)

class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','tittle','url']
    list_editable = ['tittle','url']
    ordering = ('id',)

admin.site.register(models.Permission,PermissionAdmin)
admin.site.register(models.Role)
```

## 3.插入数据
略

## 4.配置url
```python
#主urls.py中进行路由分发
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('web.urls')),
]
#web/urls.py中
from django.conf.urls import url
from web.views import customer
from web.views import payment
from web.views import account
urlpatterns = [
    url(r'^login/$',account.login),
    url(r'^index/$',account.index),

    url(r'^customer/list/$', customer.customer_list),
    url(r'^customer/add/$', customer.customer_add),
    url(r'^customer/edit/(?P<cid>\d+)/$', customer.customer_edit),
    url(r'^customer/del/(?P<cid>\d+)/$', customer.customer_del),

    url(r'^payment/list/$', payment.payment_list),
    url(r'^payment/add/$', payment.payment_add),
    url(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit),
    url(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del),
]

```
## 5.视图函数
```python
#建立views文件夹
#account.py
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
        #跨表查询获取登录用户所对应的权限
        permission =  user_obj.role.filter(permission__url__isnull=False).values('permission__url')
        print(permission)
        #设置session
        request.session['is_ok'] = True
        request.session['url'] = list(permission)
        return redirect('/index/')
    return render (request , 'login.html')

def index(request):
    """
    登录后的主页
    """
    return render(request,'index.html')
```
客户相关与付款相关省略

## 6. 完成对应的HTML页面：
略

## 7. 定义中间件
```python
# 在项目根目录下定义，middleware.py文件
from django.shortcuts import redirect,render,HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import re


class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        url = request.path_info #获取当前访问的url
        for i in settings.WHITE_LIST: #确认url是否为白名单
            if re.match(i,url):
                return 

        is_ok = request.session.get('is_ok') # 登陆验证 读取session
        if not is_ok:
            return redirect('/login/')

        for i in settings.PASS_LIST: # 确认登录后页面是否为无需权限页面
            if re.match(i,url):
                return

        permission = request.session.get('url')  #从session中读取当前用户所具有的权限
        print(permission)
        if permission:
            for i in  permission: #确认是否有访问当前页面的权限
                print(i)
                if re.match(r'^{}$'.format(i['permission__url']),url):
                    return
        return HttpResponse('无访问权限') 

```
## 8. 白名单与无需权限url
```python
#在项目settings文件中定义
WHITE_LIST = [
    r'^/login/$',
    r'^/admin/',
]

PASS_LIST = [
    r'^/index/$'
]

```
