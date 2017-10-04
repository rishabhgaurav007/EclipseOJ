# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.5 on 2017-10-04 09:55
=======
# Generated by Django 1.11.5 on 2017-10-04 09:20
>>>>>>> update_contest
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('registered_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
