# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='interval_counters',
            fields=[
                ('interval_start', models.BigIntegerField()),
                ('interval_stop', models.BigIntegerField()),
                ('count', models.IntegerField(default=0)),
                ('source', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=101, serialize=False, primary_key=True)),
            ],
        ),
    ]
