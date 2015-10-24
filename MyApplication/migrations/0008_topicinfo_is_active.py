# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0007_topicinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicinfo',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
