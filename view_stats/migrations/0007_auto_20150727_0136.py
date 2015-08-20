# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_stats', '0006_interval_counters_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interval_counters',
            name='interval_key',
            field=models.CharField(max_length=152, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='interval_counters',
            name='origin',
            field=models.CharField(max_length=60),
        ),
    ]
