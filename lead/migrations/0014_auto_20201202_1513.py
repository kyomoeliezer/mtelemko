# Generated by Django 2.2 on 2020-12-02 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0013_auto_20201202_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 15, 13, 1, 156905)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 15, 13, 1, 156546)),
        ),
    ]
