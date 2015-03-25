# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment_id', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('due_date', models.DateTimeField(verbose_name=b'Due Date')),
                ('total_grade', models.IntegerField(default=0)),
                ('course_id', models.ForeignKey(to='Course.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
