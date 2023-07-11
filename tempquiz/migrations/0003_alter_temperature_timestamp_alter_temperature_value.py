# Generated by Django 4.2.3 on 2023-07-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tempquiz", "0002_rename_time_temperature_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="temperature",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="value",
            field=models.FloatField(verbose_name=float),
        ),
    ]
