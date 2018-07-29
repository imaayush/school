# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-29 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='user',
            name='parent',
        ),
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(related_name='subjects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='parents',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='classes',
        ),
        migrations.AddField(
            model_name='subject',
            name='classes',
            field=models.ManyToManyField(related_name='subjects', to='class_room.Class'),
        ),
    ]