from django.contrib import admin
from rbac import models
# Register your models here.

admin.site.register(models.Users)

class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','tittle','url','is_menu','icon']
    list_editable = ['tittle','url','is_menu','icon']
    ordering = ('id',)

admin.site.register(models.Permission,PermissionAdmin)
admin.site.register(models.Role)