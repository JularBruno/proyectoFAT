# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-27 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlAsistencia', '0003_auto_20180627_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='origin',
            field=models.IntegerField(choices=[(0, 'Falta'), (1, 'Llegada tarde'), (2, 'Retiro anticipado')]),
        ),
    ]
