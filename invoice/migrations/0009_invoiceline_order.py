# Generated by Django 2.2 on 2020-12-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_invoiceline_ismain'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceline',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]