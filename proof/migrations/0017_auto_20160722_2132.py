# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 21:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proof', '0016_auto_20160722_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='citation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='label',
            field=models.CharField(choices=[('DE', 'Definition'), ('AX', 'Axiom'), ('TH', 'Theorem')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
