# Generated by Django 2.2 on 2021-03-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0014_auto_20210121_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='deposittype',
            field=models.CharField(choices=[('BANK', 'BANK'), ('BOTH', 'M-PESA/BANK')], default='BANK', max_length=500),
        ),
    ]
