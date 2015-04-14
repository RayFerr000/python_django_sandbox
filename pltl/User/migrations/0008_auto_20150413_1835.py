# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': ('search_users', 'Can search')},
        ),
    ]
