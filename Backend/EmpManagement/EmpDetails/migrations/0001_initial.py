# Generated by Django 5.0.2 on 2024-02-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=250)),
                ('emp_email', models.CharField(max_length=250)),
                ('emp_contact', models.CharField(max_length=250)),
                ('emp_design', models.CharField(max_length=250)),
                ('emp_salary', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
