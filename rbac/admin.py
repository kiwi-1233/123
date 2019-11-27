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