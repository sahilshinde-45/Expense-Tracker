# Generated by Django 3.2.7 on 2021-12-28 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0009_alter_add_excel_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_excel',
            name='income',
            field=models.FloatField(),
        ),
    ]