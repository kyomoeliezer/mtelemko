# Generated by Django 2.2 on 2023-01-11 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoice', '0027_auto_20230111_1826'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chartofaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('accountno', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receivedjournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=300, null=True)),
                ('cr', models.FloatField(blank=True, null=True)),
                ('dr', models.FloatField(blank=True, null=True)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rcv_champion', to='invoice.Invoice', verbose_name='Champion')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rcv_invpoice', to='invoice.Invoice', verbose_name='invoice husika')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rcv_payment', to='payment.Payment', verbose_name='Payment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=300, null=True)),
                ('cr', models.FloatField(blank=True, null=True)),
                ('dr', models.FloatField(blank=True, null=True)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jn_champion', to='invoice.Invoice', verbose_name='Champion')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jn_invpoice', to='invoice.Invoice', verbose_name='invoice husika')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jn_payment', to='payment.Payment', verbose_name='Payment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expensejournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=300, null=True)),
                ('cr', models.FloatField(blank=True, null=True)),
                ('dr', models.FloatField(blank=True, null=True)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ex_champion', to='invoice.Invoice', verbose_name='Champion')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ex_invpoice', to='invoice.Invoice', verbose_name='invoice husika')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ex_payment', to='payment.Payment', verbose_name='Payment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bankjournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=300, null=True)),
                ('cr', models.FloatField(blank=True, null=True)),
                ('dr', models.FloatField(blank=True, null=True)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_champion', to='invoice.Invoice', verbose_name='Champion')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_invpoice', to='invoice.Invoice', verbose_name='invoice husika')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_payment', to='payment.Payment', verbose_name='Payment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Accountcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('accountno', models.CharField(max_length=200, null=True)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chartofaccount', to='account.Chartofaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('accountno', models.CharField(max_length=200, null=True)),
                ('accountcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Accountcategory')),
                ('chart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Chartofaccount')),
            ],
        ),
    ]
