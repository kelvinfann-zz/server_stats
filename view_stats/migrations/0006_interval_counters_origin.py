# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_stats', '0005_auto_20150727_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='interval_counters',
            name='origin',
            field=models.CharField(default='1.txt', max_length=50),
            preserve_default=False,
        ),
    ]
