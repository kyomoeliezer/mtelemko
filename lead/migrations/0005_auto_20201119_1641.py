# Generated by Django 2.2 on 2020-11-19 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_auto_20201117_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 16, 41, 10, 37057)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='next_action',
            field=models.CharField(choices=[('', '-----'), ('call', 'Call'), ('meeting', 'Meeting'), ('reminder', 'Reminder')], default='call', max_length=30),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 16, 41, 10, 37057)),
        ),
    ]
