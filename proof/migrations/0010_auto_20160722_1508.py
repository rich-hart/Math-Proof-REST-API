# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proof', '0009_auto_20160722_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='argument',
            name='diagram',
            field=models.FileField(null=True, upload_to='/Users/openstax/workspace/Math-Proof-REST-API/data/media'),
        ),
        migrations.AlterField(
            model_name='theorem',
            name='diagram',
            field=models.FileField(null=True, upload_to='/Users/openstax/workspace/Math-Proof-REST-API/data/media'),
        ),
    ]
