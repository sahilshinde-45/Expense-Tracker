# Generated by Django 3.2.7 on 2021-12-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0011_add_excel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='income',
            field=models.FloatField(null=True),
        ),
    ]