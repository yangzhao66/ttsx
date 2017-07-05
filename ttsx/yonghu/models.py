#coding=utf-8
from django.db import models

# Create your models here.


class UserCon(models.Model):
    bname = models.CharField(max_length=20)
    pwsd = models.CharField(max_length=160)
    pmail = models.CharField(max_length=32)


class UserBuycon(models.Model):
    bpnum = models.CharField(max_length=11)
    paddr = models.CharField(max_length=500,null=True,blank=True)
    pbuy = models.CharField(max_length=500,null=True,blank=True)
    huser = models.ForeignKey('UserCon')