# Generated by Django 2.2 on 2021-02-19 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0029_auto_20210219_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 19, 15, 15, 46, 204487)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 19, 15, 15, 46, 202777)),
        ),
    ]
