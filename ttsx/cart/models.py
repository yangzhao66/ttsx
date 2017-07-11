from django.db import models
from shangpin.models import *
from yonghu.models import *
# Create your models here.


class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    def __str__(self):
        return self.user
