# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit_scrape', '0002_comment_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='link',
        ),
    ]
