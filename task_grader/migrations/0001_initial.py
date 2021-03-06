# Generated by Django 2.1.7 on 2019-04-09 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(choices=[(1, '1'), (1.5, '1+'), (1.75, '2-'), (2, '2'), (2.5, '2+'), (2.75, '3-'), (3, '3'), (3.5, '3+'), (3.75, '4-'), (4, '4'), (4.5, '4+'), (4.75, '5-'), (5, '5'), (5.5, '5+'), (5.75, '6-'), (6, '6')])),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_grader.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_grader.Recruiter'),
        ),
        migrations.AddField(
            model_name='grade',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_grader.Task'),
        ),
    ]
