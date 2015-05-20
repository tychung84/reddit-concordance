# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('body', models.CharField(max_length=500)),
                ('score_ratio', models.FloatField()),
                ('prior_score', models.IntegerField()),
                ('current_score', models.IntegerField()),
                ('subreddit', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=500)),
                ('write_time', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
