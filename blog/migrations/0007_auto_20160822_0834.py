# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 08:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160822_0456'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='Author',
        ),
        migrations.AlterModelTable(
            name='blogpost',
            table='BlogPost',
        ),
    ]