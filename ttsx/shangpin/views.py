from django.shortcuts import render
from models import *
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