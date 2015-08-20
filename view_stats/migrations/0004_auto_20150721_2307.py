# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_stats', '0003_auto_20150721_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interval_counters',
            old_name='key',
            new_name='interval_key',
        ),
    ]
