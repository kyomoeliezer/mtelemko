# Generated by Django 2.2 on 2021-06-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0018_invoice_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='show_tax',
            field=models.BooleanField(default=False),
        ),
    ]
