# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course_id',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=20),
            preserve_default=True,
        ),
    ]
