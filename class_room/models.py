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
    user_class = models.ForeignKey(Class, blank=True, null=True)
    parents = models.ManyToManyField('User', blank=True)

    class Meta:
        ordering = ('created_at',)


class Subject(BaseMixin):
    name = models.CharField(max_length=50)
    teachers = models.ManyToManyField(User, related_name="subjects")
    classes = models.ManyToManyField(Class,  related_name="subjects")

    class Meta:
        ordering = ('created_at',)


