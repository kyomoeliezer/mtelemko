# Generated by Django 2.2 on 2021-03-05 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0030_auto_20210219_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2021, 3, 5, 10, 35, 28, 392810), null=True),
        ),
    ]