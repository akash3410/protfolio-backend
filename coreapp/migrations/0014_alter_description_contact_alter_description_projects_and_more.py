# Generated by Django 4.2.2 on 2025-05-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0013_description_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='contact',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='projects',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='resume',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='service',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='skill',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='testmonial',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
