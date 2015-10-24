# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0013_topicinfo_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicinfo',
            name='topic_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
