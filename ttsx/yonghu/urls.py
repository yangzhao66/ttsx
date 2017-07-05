from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^$',views.index),
    url(r'^commit/$',views.commit),
]
