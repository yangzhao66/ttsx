from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^query/', views.query),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.goods_list),
    url(r'(\d+)/$',views.detail),
]