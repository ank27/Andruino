# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0004_question_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
    ]
