# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0015_auto_20150930_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicinfo',
            name='topic_image',
            field=models.ImageField(null=True, upload_to=b'static/images/', blank=True),
        ),
    ]
