from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^$',views.index),
    url(r'^commit/$',views.commit),
    url(r'^chachong/$',views.chachong),
    url(r'^login/$',views.login),
    url(r'^denglu/$',views.denglu),
    url(r'^center/$',views.center),
    url(r'^order/$',views.order),
    url(r'^site/$',views.site),
    url(r'^login_out/$',views.login_out)
]
