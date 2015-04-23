# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20150723_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='docket',
            name='case_name_short',
            field=models.TextField(help_text=b"The abridged name of the case, often a single word, e.g. 'Marsh'", blank=True),
        ),
        migrations.AlterField(
            model_name='docket',
            name='case_name',
            field=models.TextField(help_text=b'The standard name of the case', blank=True),
        ),
        migrations.AlterField(
            model_name='opinioncluster',
            name='source',
            field=models.CharField(blank=True, help_text=b'the source of the cluster, one of: C (court website), R (public.resource.org), CR (court website merged with resource.org), L (lawbox), LC (lawbox merged with court), LR (lawbox merged with resource.org), LCR (lawbox merged with court and resource.org), M (manual input), A (internet archive), H (brad heath archive), Z (columbia archive), ZC (columbia merged with court), ZLC (columbia merged with lawbox and court), ZLR (columbia merged with lawbox and resource.org), ZLCR (columbia merged with lawbox, court, and resource.org), ZR (columbia merged with resource.org), ZCR (columbia merged with court and resource.org), ZL (columbia merged with lawbox)', max_length=10, choices=[(b'C', b'court website'), (b'R', b'public.resource.org'), (b'CR', b'court website merged with resource.org'), (b'L', b'lawbox'), (b'LC', b'lawbox merged with court'), (b'LR', b'lawbox merged with resource.org'), (b'LCR', b'lawbox merged with court and resource.org'), (b'M', b'manual input'), (b'A', b'internet archive'), (b'H', b'brad heath archive'), (b'Z', b'columbia archive'), (b'ZC', b'columbia merged with court'), (b'ZLC', b'columbia merged with lawbox and court'), (b'ZLR', b'columbia merged with lawbox and resource.org'), (b'ZLCR', b'columbia merged with lawbox, court, and resource.org'), (b'ZR', b'columbia merged with resource.org'), (b'ZCR', b'columbia merged with court and resource.org'), (b'ZL', b'columbia merged with lawbox')]),
        ),
    ]
