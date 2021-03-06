# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-22 12:00
from __future__ import unicode_literals

from django.db import migrations, models

def add_nslcd_user(apps, schema_editor):
    try:
        group = apps.get_model("account", "bsdGroups").objects.create(
            bsdgrp_builtin=True,
            bsdgrp_gid="389",
            bsdgrp_group="nslcd"
        )
        group.save()
        user = apps.get_model("account", "bsdUsers").objects.create(
            bsdusr_builtin=True,
            bsdusr_full_name="Nslcd Daemon",
            bsdusr_group=group,
            bsdusr_home="/var/tmp/nslcd",
            bsdusr_shell="/usr/sbin/nologin",
            bsdusr_smbhash="*",
            bsdusr_unixhash="*",
            bsdusr_uid="389",
            bsdusr_username="nslcd"
        )
        user.save()

    except Exception as e:
        print("ERROR: unable to create nslcd user/group: ", e)

def remove_nslcd_user(apps, schema_editor):
    try:
        apps.get_model("account", "bsdUsers").objects.get(
            bsdusr_username="nslcd"
        ).delete()
        apps.get_model("account", "bsdGroups").objects.get(
            bsdgrp_group="nslcd"
        ).delete()

    except Exception as e:
        print("ERROR: unable to remove nslcd user/group: ", e)

class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_bsdusers_bsdusr_attributes'),
    ]

    operations = [
        migrations.RunPython(
            add_nslcd_user,
            reverse_code=remove_nslcd_user
        )
    ]
