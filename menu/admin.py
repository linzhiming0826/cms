# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from menu import models


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    ordering = ['parent']
    list_filter = ['name']
    list_display = [
        'name', 'parent', 'show', 'url', 'priority', 'code', 'icon_class'
    ]
    fields = [
        'name', 'parent', 'show', 'url', 'priority', 'code', 'icon_class'
    ]


admin.site.register(models.Menu, MenuAdmin)
