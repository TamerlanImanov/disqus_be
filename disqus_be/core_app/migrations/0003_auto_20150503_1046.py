# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_auto_20150503_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
