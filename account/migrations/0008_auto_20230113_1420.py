# Generated by Django 2.2 on 2023-01-13 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_withdraw_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankjournal',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_champion', to=settings.AUTH_USER_MODEL, verbose_name='Champion'),
        ),
        migrations.AlterField(
            model_name='bankjournal',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_invpoice', to='invoice.Invoice', verbose_name='invoice husika'),
        ),
        migrations.AlterField(
            model_name='expensejournal',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ex_champion', to=settings.AUTH_USER_MODEL, verbose_name='Champion'),
        ),
        migrations.AlterField(
            model_name='expensejournal',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ex_invpoice', to='invoice.Invoice', verbose_name='invoice husika'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jn_invpoice', to='invoice.Invoice', verbose_name='invoice husika'),
        ),
        migrations.AlterField(
            model_name='receivedjournal',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rcv_champion', to=settings.AUTH_USER_MODEL, verbose_name='Champion'),
        ),
        migrations.AlterField(
            model_name='receivedjournal',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rcv_invpoice', to='invoice.Invoice', verbose_name='invoice husika'),
        ),
    ]