# Generated by Django 2.0.1 on 2018-07-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
