# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='articletype',
            options={'verbose_name_plural': '\u6587\u7ae0\u7c7b\u578b'},
        ),
        migrations.AddField(
            model_name='articletype',
            name='introduction',
            field=models.CharField(default='\u6682\u65e0\u7b80\u4ecb', max_length=100),
        ),
    ]
