#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    good_list = []
    type_list = TypeInfo.objects.all()
    for t1 in type_list:
        nlist = t1.goodsinfo_set.order_by('-id')[0:4]
        clist = t1.goodsinfo_set.order_by('-gclick')[0:4]
        good_list.append({'t1':t1,'nlist':clist,'clist':nlist})
    context = {'goods':good_list}
    return render(request,'shangpin/index.html',context)

def query(request):
    return render(request,'shangpin/index.html')

def goods_list(request,tid,pid,sid):
    context = {}
    type = TypeInfo.objects.get(id=int(tid))
    tlist = type.goodsinfo_set.order_by('-id')[0:2]
    if int(sid) == 1:
        mlist = type.goodsinfo_set.order_by('-id')
        context['act1'] = 'active'
    elif int(sid) == 2:
        mlist = type.goodsinfo_set.order_by('-gprice')
        context['act2'] = 'active'
    else:
        mlist = type.goodsinfo_set.order_by('-gclick')
        context['act3'] = 'active'
    paginator = Paginator(mlist,3)
    pid1 = int(pid)
    print(pid1)
    if pid1 < 1:
        pid1 = 1
    elif pid1 > paginator.num_pages:
        pid1 = paginator.num_pages
    page = paginator.page(pid1)
    print(page)
    context['type'] = type
    context['tlist'] = tlist
    context['list'] = page
    context['sid'] = sid
    return render(request,'shangpin/list.html',context)

def detail(request,id): #页面详情
    try:
        goods = GoodsInfo.objects.get(id=int(id))
        type = goods.gtype
        tlist = type.goodsinfo_set.order_by('-id')[0:2]
        context = {'goods':goods,'type':type,'tlist':tlist}
        return render(request,'shangpin/detail.html',context)
    except:
        return (request,'404.html')







