# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0009_subtopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='isFormula_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='isQuestion_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='isTheory_active',
            field=models.BooleanField(default=False),
        ),
    ]
