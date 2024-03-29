# Generated by Django 2.2 on 2021-02-19 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_amount_depostedbyclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttasks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='projecttasks',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Task End date'),
        ),
        migrations.AddField(
            model_name='projecttasks',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Task start date'),
        ),
        migrations.AlterField(
            model_name='projecttasks',
            name='name',
            field=models.TextField(max_length=400, verbose_name='Task'),
        ),
        migrations.AlterField(
            model_name='projecttasks',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Taskresponsible', to=settings.AUTH_USER_MODEL),
        ),
    ]
