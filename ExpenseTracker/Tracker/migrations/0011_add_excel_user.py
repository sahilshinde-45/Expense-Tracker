# Generated by Django 3.2.7 on 2021-12-28 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0010_alter_add_excel_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_excel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Tracker.profile'),
            preserve_default=False,
        ),
    ]