# Generated by Django 2.2 on 2020-12-11 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0018_auto_20201208_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 11, 15, 59, 34, 569449)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 11, 15, 59, 34, 567914)),
        ),
        migrations.AlterField(
            model_name='targetcontact',
            name='mobile',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
