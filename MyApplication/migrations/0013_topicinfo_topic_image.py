# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0012_auto_20150924_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicinfo',
            name='topic_image',
            field=models.ImageField(null=True, upload_to=b'/static/images/', blank=True),
        ),
    ]
