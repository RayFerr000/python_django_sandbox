# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('homework_id', models.CharField(unique=True, max_length=20, db_index=True)),
                ('homework_soln', models.CharField(max_length=200)),
                ('submitted_by', models.EmailField(max_length=20)),
                ('submitted_timestamp', models.DateTimeField(verbose_name=b'date submitted')),
                ('assignment_id', models.ForeignKey(to='Assignment.Assignment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
