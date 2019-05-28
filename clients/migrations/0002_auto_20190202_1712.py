# Generated by Django 2.1.5 on 2019-02-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('clients.client',),
        ),
        migrations.AlterField(
            model_name='client',
            name='on_trial',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='paid_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]