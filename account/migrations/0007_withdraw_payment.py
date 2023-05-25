# Generated by Django 2.2 on 2023-01-13 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20230112_1812'),
        ('account', '0006_withdraw'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withdraw_payment', to='payment.Payment', verbose_name='Payment'),
        ),
    ]