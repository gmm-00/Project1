# Generated by Django 4.2.3 on 2023-07-21 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipes_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='recipes',
            new_name='Recipe',
        ),
    ]
