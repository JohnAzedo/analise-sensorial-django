# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-11 01:59
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provador',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='fabricante',
            options={'verbose_name': 'Fabricante'},
        ),
    ]
