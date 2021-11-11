# Generated by Django 3.2.9 on 2021-11-11 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crayonApp', '0003_auto_20211020_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakenQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('percentage', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_quizzes', to='crayonApp.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_quizzes', to='crayonApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='crayonApp.quiztype')),
            ],
        ),
    ]
