# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_stats', '0002_auto_20150721_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interval_counters',
            name='key',
            field=models.CharField(max_length=92, serialize=False, primary_key=True),
        ),
    ]
