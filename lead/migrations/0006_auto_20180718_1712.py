# Generated by Django 2.0.1 on 2018-07-18 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_auto_20180623_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 18, 17, 12, 40, 533038)),
        ),
    ]
