# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-23 19:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fabricante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='provador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
