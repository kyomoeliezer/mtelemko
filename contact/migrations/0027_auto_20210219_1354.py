# Generated by Django 2.2 on 2021-02-19 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0026_auto_20210219_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2021, 2, 19, 13, 54, 9, 300044), null=True),
        ),
    ]