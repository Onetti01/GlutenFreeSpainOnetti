# Generated by Django 3.2.16 on 2023-05-24 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_users_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='last_login',
        ),
    ]
