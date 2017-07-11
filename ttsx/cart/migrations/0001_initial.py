# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shangpin', '0001_initial'),
        ('yonghu', '0002_auto_20170705_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='shangpin.GoodsInfo')),
                ('user', models.ForeignKey(to='yonghu.UserInfo')),
            ],
        ),
    ]
