# coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from haystack.generic_views import SearchView
# Create your views here.


def index(request):
    good_list = []
    type_list = TypeInfo.objects.all()
    for t1 in type_list:
        nlist = t1.goodsinfo_set.order_by('-id')[0:4]
        clist = t1.goodsinfo_set.order_by('-gclick')[0:4]
        good_list.append({'t1': t1, 'nlist': clist, 'clist': nlist})
    context = {'goods': good_list}
    return render(request, 'shangpin/index.html', context)


def query(request):
    return render(request, 'shangpin/index.html')


def goods_list(request, tid, pid, sid):
    context = {}
    desc = request.GET.get('desc', '1')
    type = TypeInfo.objects.get(id=int(tid))
    tlist = type.goodsinfo_set.order_by('-id')[0:2]
    if int(sid) == 1:
        mlist = type.goodsinfo_set.order_by('-id')
        context['act1'] = 'active'
    elif int(sid) == 2:
        if desc == '1':
            mlist = type.goodsinfo_set.order_by('-gprice')
            #desc = '0'
        else:
            mlist = type.goodsinfo_set.order_by('gprice')
            #desc = '1'
        context['act2'] = 'active'
    else:
        mlist = type.goodsinfo_set.order_by('-gclick')
        context['act3'] = 'active'
    paginator = Paginator(mlist, 15)
    pid1 = int(pid)
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
    context['desc'] = desc
    return render(request, 'shangpin/list.html', context)


def detail(request, id):  # 页面详情
    try:
        history = request.session.get('history', [])
        goods = GoodsInfo.objects.get(id=int(id))
        goods.gclick += 1
        goods.save()
        type = goods.gtype
        tlist = type.goodsinfo_set.order_by('-id')[0:2]
        context = {'goods': goods, 'type': type, 'tlist': tlist}
        if len(history) == 5:
            history.pop(0)
        history.append(int(id))
        request.session['history'] = history
        return render(request, 'shangpin/detail.html', context)
    except BaseException:
        return (request, '404.html')


class MySearchView(SearchView):
    """My custom search view."""

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        page_range = []
        page = context.get('page_obj')
        if page.paginator.num_pages < 5:
            page_range = page.paginator.page_range
        elif page.number <= 2:
            page_range = range(1, 6)
        elif page.number >= page.paginator.num_pages - 1:
            page_range = range(
                page.paginator.num_pages - 4,
                page.paginator.num_pages + 1)
        else:
            page_range = range(page.number - 2, page.number + 3)
        context['page_range'] = page_range
        return context
