# Generated by Django 2.0.1 on 2018-07-18 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20180718_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2018, 7, 18, 17, 50, 1, 282607), null=True),
        ),
    ]
