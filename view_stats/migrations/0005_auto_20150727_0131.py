# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_stats', '0004_auto_20150721_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interval_counters',
            old_name='source',
            new_name='server',
        ),
    ]
