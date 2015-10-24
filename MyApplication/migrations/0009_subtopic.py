# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0008_topicinfo_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subTopic_name', models.CharField(max_length=50)),
                ('subTopic_isactive', models.BooleanField(default=False)),
                ('topic', models.ForeignKey(to='MyApplication.TopicInfo')),
            ],
        ),
    ]
