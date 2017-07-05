from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def register(request):
    return render(request,'yonghu/register.html')


def commit(request):
    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    uemail = dict.get('email')
    if UserCon.objects.exists()
        user = UserCon()
        user.bname = uname
        user.pwsd = upwd
        user.pmail = uemail
        user.save()
    return redirect('/')
def index(request):
    return render(request,'yonghu/index.html')