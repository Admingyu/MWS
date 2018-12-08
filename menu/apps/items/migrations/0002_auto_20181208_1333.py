# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-08 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': '项目', 'verbose_name_plural': '项目'},
        ),
        migrations.AddField(
            model_name='item',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
