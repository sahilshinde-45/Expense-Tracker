# Generated by Django 3.2.7 on 2021-12-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0008_add_excel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_excel',
            name='income',
            field=models.FloatField(default=0),
        ),
    ]
