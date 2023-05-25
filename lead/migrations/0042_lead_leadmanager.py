# Generated by Django 2.2 on 2021-08-12 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead', '0041_targetcontact_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='leadmanager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leadmanager', to=settings.AUTH_USER_MODEL),
        ),
    ]
