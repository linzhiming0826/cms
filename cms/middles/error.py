# -*- coding: utf-8 -*-
import sys
from django.views.debug import technical_500_response
from django.conf import settings
from cms.apis.menus import Menus


class ErrorMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        # 如果关闭debug模式，并且是管理员：可以看到错误页面，否则根据系统配置进行跳转。
        if settings.DEBUG is False and request.user.is_superuser:
            return technical_500_response(request, *sys.exc_info())
