# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 19:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=datetime.datetime(2016, 5, 29, 19, 14, 56, 312683, tzinfo=utc), height_field=100, upload_to='', width_field=100),
            preserve_default=False,
        ),
    ]
