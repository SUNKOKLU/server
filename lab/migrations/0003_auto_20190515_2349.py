# Generated by Django 2.2.1 on 2019-05-15 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
        ('user', '0001_initial'),
        ('lab', '0002_auto_20190515_2349'),
        ('course', '0002_auto_20190515_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='labsubmission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student'),
        ),
        migrations.AddField(
            model_name='labproblem',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Lab'),
        ),
        migrations.AddField(
            model_name='labproblem',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem'),
        ),
        migrations.AddField(
            model_name='lab',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AddField(
            model_name='lab',
            name='problems',
            field=models.ManyToManyField(blank=True, related_name='labs', through='lab.LabProblem', to='problem.Problem'),
        ),
        migrations.AddField(
            model_name='lab',
            name='resources',
            field=models.ManyToManyField(blank=True, related_name='labs', to='course.CourseResource'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='lab_submission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab.LabSubmission'),
        ),
    ]
