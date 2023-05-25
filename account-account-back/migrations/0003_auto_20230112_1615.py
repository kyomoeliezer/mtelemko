# Generated by Django 2.2 on 2023-01-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20230112_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_bankaccount',
            field=models.BooleanField(default=False, verbose_name='Is Bank Account'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_cashaccount',
            field=models.BooleanField(default=False, verbose_name='Is Cash Account'),
        ),
    ]
