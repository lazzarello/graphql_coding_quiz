# Generated by Django 4.2.3 on 2023-07-07 22:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tempquiz", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="temperature",
            old_name="time",
            new_name="timestamp",
        ),
        migrations.RenameField(
            model_name="temperature",
            old_name="temperature",
            new_name="value",
        ),
    ]