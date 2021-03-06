# Generated by Django 2.2.1 on 2019-05-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.TextField(blank=True)),
                ('output', models.TextField(blank=True)),
                ('type', models.BooleanField()),
                ('weight', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('runtime_limit', models.BigIntegerField()),
                ('memory_limit', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='problems', to='problem.Tag')),
            ],
        ),
    ]
