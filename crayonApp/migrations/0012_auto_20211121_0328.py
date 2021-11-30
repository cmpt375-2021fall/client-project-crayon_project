# Generated by Django 3.2.6 on 2021-11-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crayonApp', '0011_auto_20211121_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='id',
        ),
        migrations.AddField(
            model_name='file',
            name='f_id',
            field=models.CharField(default='e98e039c', editable=False, max_length=256, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='4132e5cf', editable=False, max_length=256, primary_key=True, serialize=False, unique=True),
        ),
    ]