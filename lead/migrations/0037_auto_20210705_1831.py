# Generated by Django 2.2 on 2021-07-05 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0036_auto_20210629_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 18, 31, 9, 819384)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 18, 31, 9, 819384)),
        ),
    ]
