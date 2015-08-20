# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interval_counters',
            name='key',
            field=models.CharField(max_length=90, serialize=False, primary_key=True),
        ),
    ]
