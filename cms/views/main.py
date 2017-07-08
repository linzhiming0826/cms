# encoding:utf-8
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cms.apis.menus import Menus


@login_required(login_url='/login')
def index(request):
    '''首页'''
    data = {'menus': Menus().get_menus(request), 'code': 'index'}
    return render(request, 'index.html', data)


def sign_in(request):
    '''登录api'''
    username = request.POST['userName']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    result = {'code': 0, 'msg': ''}
    if user:
        if user.is_active:
            login(request, user)
            result['code'] = 1
            result['msg'] = u'成功'
        else:
            result['msg'] = u'该用户还没有激活，请联系管理员'
    else:
        result['msg'] = u'账户名或者密码错误'
    return HttpResponse(json.dumps(result), content_type="application/json")


def login_page(request):
    '''登录页面'''
    return render(request, 'login.html')


@login_required(login_url='/login')
def sign_out(request):
    '''退出登录'''
    logout(request)
    result = {'code': 1, 'msg': 'success'}
    return HttpResponse(json.dumps(result), content_type="application/json")


@login_required(login_url='/login')
def article(request):
    '''文章列表'''
    data = {'menus': Menus().get_menus(request), 'code': 'data_article'}
    return render(request, 'article.html', data)
