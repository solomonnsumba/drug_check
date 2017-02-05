# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('drug_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('manufacturer', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('exp_date', models.CharField(max_length=20)),
                ('thumb_nail', models.ImageField(upload_to=b'photos/')),
            ],
        ),
    ]
