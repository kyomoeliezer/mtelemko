# Generated by Django 2.2 on 2021-02-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20210219_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttasks',
            name='desc',
            field=models.CharField(max_length=400, null=True, verbose_name='Desc'),
        ),
    ]