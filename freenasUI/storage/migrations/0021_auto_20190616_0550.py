# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-06-16 05:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0020_auto_20190402_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='replication',
            name='repl_state',
            field=models.TextField(default='{}', editable=False),
        ),
    ]
