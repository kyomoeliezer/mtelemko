# Generated by Django 2.2 on 2020-11-20 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20201120_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2020, 11, 20, 10, 17, 28, 305167), null=True),
        ),
    ]
