# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-03 09:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170803_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
