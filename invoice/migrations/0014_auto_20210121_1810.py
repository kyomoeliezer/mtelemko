# Generated by Django 2.2 on 2021-01-21 15:10

from django.db import migrations, models
import invoice.models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0013_invoice_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='file',
            field=models.FileField(null=True, upload_to=invoice.models.content_file_name_invo),
        ),
    ]
