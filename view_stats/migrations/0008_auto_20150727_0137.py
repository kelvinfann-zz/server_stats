# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_stats', '0007_auto_20150727_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interval_counters',
            name='interval_key',
            field=models.CharField(max_length=142, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='interval_counters',
            name='origin',
            field=models.CharField(max_length=50),
        ),
    ]
