# Generated by Django 3.2.7 on 2021-12-28 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0013_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_excel',
            name='user',
        ),
    ]
