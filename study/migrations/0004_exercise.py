# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_wordbank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('Type', models.IntegerField(choices=[(1, 'Choices'), (2, 'Find the Mistake'), (3, 'Situations'), (4, 'Translation'), (5, 'Story')])),
            ],
        ),
    ]
