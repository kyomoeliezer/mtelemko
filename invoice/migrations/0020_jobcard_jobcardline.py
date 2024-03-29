# Generated by Django 2.2 on 2021-07-05 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoice', '0019_invoice_show_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=300, verbose_name='Project Title')),
                ('device', models.CharField(max_length=300, verbose_name='Device(s)')),
                ('client', models.CharField(max_length=300, verbose_name='Client Name')),
                ('address', models.CharField(max_length=300, verbose_name='Client Address')),
                ('city', models.CharField(max_length=300, verbose_name='Client City')),
                ('technician', models.CharField(max_length=300, verbose_name='Technician/Engineer')),
                ('job_date', models.DateField(null=True, verbose_name='Activities End Date')),
                ('jobno', models.CharField(max_length=30, verbose_name='Job no')),
                ('jobcard_no', models.CharField(max_length=30, verbose_name='Jobcard Number')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.Invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobcardLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('device', models.CharField(max_length=200, verbose_name='Devices')),
                ('desc', models.CharField(max_length=200, verbose_name='Description')),
                ('status', models.IntegerField(default=1, verbose_name='1:done,0:onprogress, 10:is a device')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('jobcard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.Jobcard')),
            ],
        ),
    ]
