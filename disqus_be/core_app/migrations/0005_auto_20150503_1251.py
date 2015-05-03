# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0004_auto_20150503_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author_title',
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(default=1, unique=True, max_length=1000, blank=True),
            preserve_default=False,
        ),
    ]
