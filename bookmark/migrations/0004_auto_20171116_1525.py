# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_bookmark_visiters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='visiters',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
