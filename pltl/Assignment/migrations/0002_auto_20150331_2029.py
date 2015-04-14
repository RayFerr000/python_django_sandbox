# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Date Published'),
            preserve_default=True,
        ),
    ]
