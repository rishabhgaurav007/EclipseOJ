# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 09:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0003_auto_20171004_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 9, 14, 33, 828195, tzinfo=utc)),
        ),
    ]
