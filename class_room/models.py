# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from mixins import BaseMixin

USER_TYPE = (("PARENT", "PARENT"),
             ("TEACHER", "TEACHER"),
             ("STUDENT", "STUDENT"))


class Class(BaseMixin):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('created_at',)


class User(AbstractUser, BaseMixin):
    user_type = models.CharField(choices=USER_TYPE, max_length=20, default=USER_TYPE[2][0])
    classes = models.ManyToManyField(Class)
    parent = models.ForeignKey('User', blank=True, null=True)

    class Meta:
        ordering = ('created_at',)


class Subject(BaseMixin):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User,  on_delete=models.CASCADE)
    classes = models.ForeignKey(Class)

    class Meta:
        ordering = ('created_at',)


