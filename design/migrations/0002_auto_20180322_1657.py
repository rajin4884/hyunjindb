# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 07:57
from __future__ import unicode_literals

import design.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designphoto',
            name='image',
            field=design.fields.ThumbnailImageField(upload_to='photo/%Y/%m'),
        ),
    ]
