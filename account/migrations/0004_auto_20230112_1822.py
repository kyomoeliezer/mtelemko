# Generated by Django 2.2 on 2023-01-12 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20230112_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='champion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jn_champion', to=settings.AUTH_USER_MODEL, verbose_name='Champion'),
        ),
    ]
