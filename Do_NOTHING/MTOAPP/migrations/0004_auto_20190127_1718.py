# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-27 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MTOAPP', '0003_auto_20190127_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ForeignKey(null=True, on_delete=models.SET(4), to='MTOAPP.Student'),
        ),
    ]
