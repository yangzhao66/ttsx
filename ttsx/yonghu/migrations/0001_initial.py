# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBuycon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bpnum', models.CharField(max_length=11)),
                ('paddr', models.CharField(max_length=500, null=True, blank=True)),
                ('pbuy', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bname', models.CharField(max_length=20)),
                ('pwsd', models.CharField(max_length=160)),
                ('pmail', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='userbuycon',
            name='huser',
            field=models.ForeignKey(to='yonghu.UserCon'),
        ),
    ]
