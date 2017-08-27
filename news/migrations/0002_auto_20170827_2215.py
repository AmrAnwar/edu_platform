# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-27 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field_image', null=True, upload_to=news.models.upload_location, width_field='width_field_image'),
        ),
    ]
