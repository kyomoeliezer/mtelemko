# Generated by Django 2.2 on 2020-11-20 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_auto_20201120_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2020, 11, 20, 12, 10, 15, 293733), null=True),
        ),
    ]