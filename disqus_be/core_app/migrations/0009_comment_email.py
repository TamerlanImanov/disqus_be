# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0008_comment_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
