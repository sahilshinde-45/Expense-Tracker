# Generated by Django 3.2.7 on 2021-12-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='income',
            field=models.FloatField(),
        ),
    ]