# Generated by Django 2.2.1 on 2019-05-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('submission', '0001_initial'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentexam',
            name='problem_submissions',
            field=models.ManyToManyField(blank=True, related_name='student_exams', to='submission.ProblemSubmission'),
        ),
    ]
