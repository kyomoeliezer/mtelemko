# Generated by Django 2.2 on 2020-12-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_invoice_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceline',
            name='ismain',
            field=models.BooleanField(default=False),
        ),
    ]