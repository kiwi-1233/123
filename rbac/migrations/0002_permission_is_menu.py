# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-28 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='是否为菜单'),
        ),
    ]