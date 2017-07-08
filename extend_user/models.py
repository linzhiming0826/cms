# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


# 继承AbstractUser类，实际上django的User也是继承他，我们要做的就是用自己的类代替django自己的User
class MyUser(AbstractUser):
    name = models.CharField(
        u'name', max_length=32, blank=False, null=False, default='')
    icon = models.CharField(
        u'icon', max_length=200, blank=False, null=False, default='')
