# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 10:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profilePic',
            new_name='profilePics',
        ),
    ]