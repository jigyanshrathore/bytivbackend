# Generated by Django 5.1.4 on 2025-01-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in-progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=20)),
            ],
        ),
    ]
