# Generated by Django 2.2 on 2020-11-24 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0011_auto_20201120_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 16, 53, 9, 311942)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 16, 53, 9, 311607)),
        ),
    ]
