# Generated by Django 3.0.7 on 2020-07-18 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disdata', '0009_auto_20200716_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disdata.Disease'),
        ),
    ]