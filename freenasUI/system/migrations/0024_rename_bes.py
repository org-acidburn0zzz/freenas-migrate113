# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-03 12:54
from __future__ import unicode_literals

from django.db import migrations
import os
import subprocess


def rename_bes(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0023_merge_20180612_2359'),
    ]

    operations = [
        migrations.RunPython(rename_bes, reverse_code=migrations.RunPython.noop),
    ]