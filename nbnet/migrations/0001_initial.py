# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.CharField(max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
