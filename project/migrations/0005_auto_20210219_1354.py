# Generated by Django 2.2 on 2021-02-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210219_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttasks',
            name='name',
            field=models.CharField(max_length=400, verbose_name='Task'),
        ),
    ]
