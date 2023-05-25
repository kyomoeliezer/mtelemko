# Generated by Django 2.2 on 2020-11-17 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_auto_20201117_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='next_action',
            field=models.CharField(choices=[('call', 'Call'), ('meeting', 'Meeting'), ('reminder', 'Reminder')], default='call', max_length=30),
        ),
        migrations.AddField(
            model_name='lead',
            name='next_action_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 17, 18, 29, 32, 311881)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 17, 18, 29, 32, 310882)),
        ),
    ]