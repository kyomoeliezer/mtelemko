# Generated by Django 2.2 on 2023-01-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
