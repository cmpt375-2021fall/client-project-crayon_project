# Generated by Django 3.2.6 on 2021-11-09 10:06

import crayonApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crayonApp', '0004_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to=crayonApp.models.user_directory_path)),
                ('upload_method', models.CharField(max_length=20, verbose_name='Upload Method')),
            ],
        ),
    ]