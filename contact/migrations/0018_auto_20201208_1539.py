# Generated by Django 2.2 on 2020-12-08 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0017_auto_20201208_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(blank='', default=datetime.datetime(2020, 12, 8, 15, 39, 18, 344643), null=True),
        ),
    ]
