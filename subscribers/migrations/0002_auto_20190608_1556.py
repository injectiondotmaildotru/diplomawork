# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-08 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='Speciality',
            new_name='speciality',
        ),
    ]