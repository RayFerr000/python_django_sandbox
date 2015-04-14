# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20150413_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('search_users', 'Can search'),)},
        ),
    ]
