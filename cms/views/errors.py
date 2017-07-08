# encoding:utf-8
from django.shortcuts import render


def page_not_found(request):
    '''404页面'''
    return render(request, 'errors/404.html')


def server_error(request):
    '''500页面'''
    return render(request, 'errors/500.html')