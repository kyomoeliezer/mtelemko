# Generated by Django 2.2 on 2021-01-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201130_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='amount_depostedbyclient',
            field=models.FloatField(null=True, verbose_name='Payment after Tax'),
        ),
    ]
