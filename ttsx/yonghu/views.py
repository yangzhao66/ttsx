# coding=utf-8
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from hashlib import sha1
from user_decrators import *
from shangpin.models import *
# Create your views here.


def register(request):
    return render(request, 'yonghu/register.html')


def commit(request):  # 用户注册提交
    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    umail = dict.get('email')
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.umail = umail
    user.save()
    return redirect('/user/center/')


def chachong(request):  # 判断注册名是否重复
    uname = request.GET.get('uname')
    result = UserInfo.objects.filter(uname=uname).count()
    context = {'valid': result}
    return JsonResponse(context)


@user_login
def center(request):  # 用户中心
    user = UserInfo.objects.get(pk=request.session['uid'])
    history = request.session.get('history')
    hisgoods = []
    history = history[::-1]
    for hid in history:
        goods = GoodsInfo.objects.get(id=hid)
        hisgoods.append(goods)
    context = {'user': user, 'history': hisgoods}
    return render(request, 'yonghu/center.html', context)


@user_login
def order(request):  # 订单中心
    return render(request, 'yonghu/order.html')


@user_login
def site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.ucode = post.get('ucode')
        user.uphone = post.get('uphone')
        user.save()
    context = {'user': user}
    return render(request, 'yonghu/site.html', context)


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'na': uname}
    return render(request, 'yonghu/login.html', context)


def denglu(request):  # 用来进行登陆验证
    dict = request.POST
    uname = dict.get('user_name')
    print(uname)
    upwd = dict.get('user_pwd')
    btn = dict.get('remember', '0')
    s1 = sha1()
    s1.update(upwd)
    upwd1 = s1.hexdigest()
    if UserInfo.objects.filter(uname=uname).exists():
        user = UserInfo.objects.filter(uname=uname)
        if user[0].upwd == upwd1:  # 验证通过
            request.session['uid'] = user[0].id
            request.session['uname'] = uname
            path = request.session.get('url_path', '/')
            response = redirect(path)
            if btn == '1':
                response.set_cookie('uname', uname)
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:  # 密码错误
            context = {'val': 1, 'na': uname, 'password': upwd}
            return render(request, 'yonghu/login.html', context)
    else:
        context = {'val': 2, 'na': uname, 'password': upwd}
        return render(request, 'yonghu/login.html', context)


def login_out(request):
    request.session.flush()
    return redirect('/')


@user_login
def cart(request):
    return render(request, 'yonghu/cart.html')
