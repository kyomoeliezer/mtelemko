# Generated by Django 2.2 on 2021-01-21 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0024_auto_20210121_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2021, 1, 21, 18, 10, 15, 488976), null=True),
        ),
    ]