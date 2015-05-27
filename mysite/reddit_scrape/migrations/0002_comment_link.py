# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit_scrape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='link',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
