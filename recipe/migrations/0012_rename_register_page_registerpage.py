# Generated by Django 4.2.3 on 2023-07-24 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_remove_register_page_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register_page',
            new_name='RegisterPage',
        ),
    ]
