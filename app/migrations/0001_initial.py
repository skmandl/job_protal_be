# Generated by Django 2.2 on 2020-06-06 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.TextField(max_length=800)),
                ('salary_from', models.PositiveIntegerField()),
                ('salary_to', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Responsibilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('job_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.JobDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Recuirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('job_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.JobDetail')),
            ],
        ),
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('last_date', models.DateField(blank=True, null=True)),
                ('apply_link', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Company')),
                ('degree', models.ManyToManyField(to='app.Degree')),
                ('description', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.JobDetail')),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.JobType')),
            ],
        ),
    ]