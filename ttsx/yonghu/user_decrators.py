# coding=utf-8
from django.shortcuts import redirect


def user_login(func):
    def func1(request, *args, **kwargs):
        if 'uid' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')
    return func1
