# Generated by Django 4.2.2 on 2025-04-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0003_remove_education_running_alter_education_end'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
    ]
