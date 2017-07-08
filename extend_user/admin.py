# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from extend_user import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# custom user admin
class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)


class MyUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(CustomUserAdmin, self).__init__(*args, **kwargs)
        self.list_display = ('username', 'name', 'icon', 'email', 'is_active',
                             'is_staff', 'is_superuser')
        self.search_fields = ('username', 'email', 'name')
        self.form = MyUserChangeForm
        self.add_form = MyUserCreationForm

    def changelist_view(
            self, request, extra_context=None
    ):
        if not request.user.is_superuser:
            self.fieldsets = (
                (None, {
                    'fields': ('username', 'password', )
                }),
                (_('Personal info'), {
                    'fields': ('name', 'icon', 'email')
                }),
                (_('Permissions'), {
                    'fields': ('is_active', 'is_staff', 'groups')
                }),
                (_('Important dates'), {
                    'fields': ('last_login', 'date_joined')
                }),
            )
            self.add_fieldsets = ((None, {
                'classes': ('wide', ),
                'fields':
                ('username', 'name', 'icon', 'password1', 'password2', 'email',
                 'is_active', 'is_staff', 'groups'),
            }), )
        else:
            self.fieldsets = ((None, {
                'fields': ('username', 'password', )
            }), (_('Personal info'), {
                'fields': ('name', 'icon', 'email')
            }), (_('Permissions'), {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')
            }), (_('Important dates'), {
                'fields': ('last_login', 'date_joined')
            }), )
            self.add_fieldsets = ((None, {
                'classes': ('wide', ),
                'fields':
                ('username', 'name', 'icon', 'password1', 'password2', 'email',
                 'is_active', 'is_staff', 'is_superuser', 'groups'),
            }), )
        return super(CustomUserAdmin, self).changelist_view(
            request, extra_context)


admin.site.register(models.MyUser, CustomUserAdmin)
