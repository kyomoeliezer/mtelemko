# Generated by Django 2.2 on 2020-12-17 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0020_auto_20201215_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 16, 0, 37, 656891)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 16, 0, 37, 655483)),
        ),
    ]
