# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0010_auto_20150924_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='isFormula_active',
            field=models.BooleanField(default=False, verbose_name=b'Formula'),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='isQuestion_active',
            field=models.BooleanField(default=False, verbose_name=b'Question'),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='isTheory_active',
            field=models.BooleanField(default=False, verbose_name=b'Theory'),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='subTopic_isactive',
            field=models.BooleanField(default=False, verbose_name=b'Active'),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='subTopic_name',
            field=models.CharField(max_length=50, verbose_name=b'Sub Topic Name'),
        ),
    ]
