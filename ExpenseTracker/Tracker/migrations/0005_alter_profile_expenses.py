# Generated by Django 3.2.7 on 2021-12-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0004_alter_tracker_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(default=0),
        ),
    ]
