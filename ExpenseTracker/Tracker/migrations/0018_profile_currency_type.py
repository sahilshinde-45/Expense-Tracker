# Generated by Django 3.2.7 on 2022-01-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0017_alter_add_excel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='currency_type',
            field=models.CharField(default='EUR', max_length=100),
        ),
    ]
