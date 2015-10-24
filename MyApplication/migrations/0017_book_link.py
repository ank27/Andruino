# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0016_auto_20150930_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('number_of_pages', models.CharField(max_length=10, null=True)),
                ('size', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(null=True, upload_to=b'static/ebooks/images/', blank=True)),
                ('isbn', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_text', models.CharField(max_length=1000)),
                ('book', models.ForeignKey(verbose_name=b'Book', to='MyApplication.Book')),
            ],
        ),
    ]
