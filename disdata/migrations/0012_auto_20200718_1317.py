# Generated by Django 3.0.7 on 2020-07-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disdata', '0011_report_report_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='animal_infection',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='human_infection',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
