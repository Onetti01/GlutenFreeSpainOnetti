# Generated by Django 3.2.16 on 2023-05-28 20:42

import apps.Sponsors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sponsors', '0002_alter_sponsors_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsors',
            name='icon',
            field=models.ImageField(upload_to=apps.Sponsors.models.rename_icon),
        ),
    ]
