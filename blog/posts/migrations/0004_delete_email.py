# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]
