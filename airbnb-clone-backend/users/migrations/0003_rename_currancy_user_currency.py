# Generated by Django 4.1.7 on 2023-03-20 00:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_is_host"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="currancy",
            new_name="currency",
        ),
    ]
