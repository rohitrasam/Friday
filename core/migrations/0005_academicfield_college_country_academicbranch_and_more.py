# Generated by Django 5.0.6 on 2024-06-21 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_mcq_question_ptr_alter_department_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('acceptance_rate', models.IntegerField(null=True)),
                ('highest_degree', models.IntegerField(choices=[(0, 'Bachelors'), (1, 'Masters'), (2, 'PHD')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AcademicBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.academicfield')),
            ],
        ),
        migrations.CreateModel(
            name='BranchRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.academicbranch')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.college')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='country_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country'),
        ),
        migrations.CreateModel(
            name='FieldRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.college')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.academicfield')),
            ],
        ),
        migrations.CreateModel(
            name='MCQResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.question')),
            ],
        ),
        migrations.DeleteModel(
            name='CodingQuestions',
        ),
    ]