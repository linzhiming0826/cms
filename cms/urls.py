# encoding:utf-8
from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^index$', main.index), url(r'^login$', main.login_page), url(
        r'^admin/', admin.site.urls), url(r'^signIn$', main.sign_in), url(
            r'^$', main.index), url(r'^signOut$', main.sign_out), url(
                r'^article$', main.article), url(
                    r'^favicon\.ico$',
                    RedirectView.as_view(url='/static/assets/i/favicon.png')),
]
