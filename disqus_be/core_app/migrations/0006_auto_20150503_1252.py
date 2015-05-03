# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0005_auto_20150503_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
    ]
