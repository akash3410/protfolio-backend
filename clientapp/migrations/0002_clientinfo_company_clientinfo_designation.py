# Generated by Django 4.2.2 on 2025-04-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
