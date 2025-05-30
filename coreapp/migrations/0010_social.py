# Generated by Django 4.2.2 on 2025-04-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0009_delete_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
