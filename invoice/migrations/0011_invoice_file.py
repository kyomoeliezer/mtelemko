# Generated by Django 2.2 on 2021-01-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_invoice_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
