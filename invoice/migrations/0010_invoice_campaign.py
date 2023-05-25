# Generated by Django 2.2 on 2020-12-17 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0021_auto_20201217_1600'),
        ('invoice', '0009_invoiceline_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lead.Campaign', verbose_name='Campaign'),
        ),
    ]
