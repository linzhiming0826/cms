# encoding:utf-8
from django.shortcuts import render


def test(request):
    context = {'name': 'TuoX'}
    return render(request, 'test.html', context)