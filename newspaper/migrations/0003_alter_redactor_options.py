# Generated by Django 5.1.1 on 2024-10-06 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newspaper", "0002_alter_redactor_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="redactor",
            options={"verbose_name": "redactor", "verbose_name_plural": "redactors"},
        ),
    ]
