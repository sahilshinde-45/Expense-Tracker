# Generated by Django 3.2.7 on 2021-12-24 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0003_tracker_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tracker.profile'),
        ),
    ]
