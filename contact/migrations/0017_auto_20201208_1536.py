# Generated by Django 2.2 on 2020-12-08 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0016_auto_20201208_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2020, 12, 8, 15, 36, 14, 169288), null=True),
        ),
    ]