# Generated by Django 3.2.16 on 2023-05-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bills', '0002_remove_bills_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='expiration_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='bills',
            name='subscription_date',
            field=models.DateField(default=None),
        ),
    ]
