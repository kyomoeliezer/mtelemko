# Generated by Django 2.2 on 2023-01-13 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20230113_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jn_champion', to=settings.AUTH_USER_MODEL, verbose_name='Champion'),
        ),
    ]
