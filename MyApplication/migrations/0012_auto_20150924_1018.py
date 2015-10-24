# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0011_auto_20150924_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(verbose_name=b'Topic Name', to='MyApplication.TopicInfo'),
        ),
    ]
