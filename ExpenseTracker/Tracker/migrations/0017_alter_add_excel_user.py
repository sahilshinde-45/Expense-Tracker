# Generated by Django 3.2.7 on 2021-12-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0016_alter_add_excel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_excel',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]