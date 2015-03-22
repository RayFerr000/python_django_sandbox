# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20150319_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Fname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Lname',
            new_name='lname',
        ),
        migrations.AddField(
            model_name='user',
            name='course_id',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=20, db_index=True),
            preserve_default=True,
        ),
    ]
