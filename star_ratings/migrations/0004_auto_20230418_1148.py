# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('star_ratings', '0003_auto_20160721_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='id',
        ),
    ]
