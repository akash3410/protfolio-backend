# Generated by Django 4.2.2 on 2025-04-30 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='resopned',
            new_name='responed',
        ),
    ]
