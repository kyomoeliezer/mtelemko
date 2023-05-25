# Generated by Django 2.2 on 2021-08-11 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead', '0039_auto_20210705_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followup', models.TextField(max_length=200, verbose_name='Follup Note')),
                ('followup_date', models.DateField(verbose_name='Follup date')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='FiledBy', to=settings.AUTH_USER_MODEL)),
                ('followup_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='responsible', to=settings.AUTH_USER_MODEL)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lead.Lead')),
            ],
        ),
    ]