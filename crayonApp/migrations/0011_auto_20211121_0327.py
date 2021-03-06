# Generated by Django 3.2.6 on 2021-11-21 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crayonApp', '0010_auto_20211120_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='room_id',
        ),
        migrations.RemoveField(
            model_name='file',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='6016c046', editable=False, max_length=256, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='File_attr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crayonApp.room')),
                ('user_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crayonApp.user')),
            ],
        ),
    ]
