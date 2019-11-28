# 一级菜单流程
## 访问流程
    1，登录
    2. rbac下的中间件通过白名单进入登陆页面
    3. 进入login视图函数完成账户校验
    4. 进入权限信息初始化
    5. 通过中间件中的无需权限页面，进入首页
    6. 访问任意地址
        7. 进入权限信息校验：
            - 有权限：正常显示页面
            - 无权限：返回HttpRsponse对象提示无权限
##左侧菜单
    1. 在layout.html文件使用menu includetag
        1. menu 在rbac/tamplatetags下的rbac中声明
        2. 在其中处理菜单选中效果
        3.返回至。/rbac/templates/menu.html
        
# 使用
1.在settings中注册app
2.在settings中注册中间件
    ```python
    MIDDLEWARE = [
     ...
    'rbac.middleware.rbac_middlewares.AuthMiddleware'
    ]
    
    ```
3. 权限信息配置
```python
#白名单
WHITE_LIST = [
    r'^/login/$',
    r'^/admin/',
]
#免认证名单
PASS_LIST = [
    r'^/index/$'
]

#权限的session_key
PERMISSION_SESSION_KEY = 'permission'
#菜单的session_key
MENU_SESSION_KEY = 'menu'

```
4. 完成表关系建立及数据库迁移:
    - 在rbac下的migrationgs中清除__init__以外的所有py文件
    - 执行数据库迁移命令
        - python manage.py make migrations
        - python manage.py migrate
5. 使用admin填充数据
    - 权限信息
    - 角色信息
    - 用户信息
    
6.登录成功后的权限信息初始化
    ```python
    from rbac.service.permission_init import permission_init
    #登陆成功后的权限信息初始化
    permission_init(request,user_obj)
    ```
    
7. 动态生成一级菜单
    - 在母板中左侧菜单的位置
    ```html
    <div class="left-menu">
        <div class="menu-body">
            {% load rabc %}
            {% menu request %}
        </div>
    </div>
    ```
   - 引入css样式
   ```html
    <link rel="stylesheet" href={% static 'rbac/css/left_menu.css' %}>
   ```
      
