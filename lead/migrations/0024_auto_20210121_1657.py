# Generated by Django 2.2 on 2021-01-21 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0023_auto_20210120_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 16, 57, 33, 168155)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 16, 57, 33, 166047)),
        ),
    ]
