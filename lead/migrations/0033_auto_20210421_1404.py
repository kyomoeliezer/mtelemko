# Generated by Django 2.2 on 2021-04-21 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0032_auto_20210421_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 14, 3, 59, 161775)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 14, 3, 59, 159896)),
        ),
    ]
