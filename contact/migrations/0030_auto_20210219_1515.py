# Generated by Django 2.2 on 2021-02-19 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0029_auto_20210219_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2021, 2, 19, 15, 15, 46, 198213), null=True),
        ),
    ]
