# Generated by Django 3.1.5 on 2021-03-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('about', models.CharField(max_length=300)),
                ('job_title', models.CharField(max_length=40)),
                ('company_name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=300)),
                ('education_qualification', models.CharField(max_length=70)),
                ('skills', models.CharField(max_length=200)),
            ],
        ),
    ]