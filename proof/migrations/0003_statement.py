# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proof', '0002_auto_20160720_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_string', models.TextField()),
            ],
        ),
    ]