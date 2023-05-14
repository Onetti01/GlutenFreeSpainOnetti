# Generated by Django 3.2.16 on 2023-05-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('CIF', models.TextField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('icon', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Sponsors',
            },
        ),
    ]