# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-24 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=50)),
                ('subject_name', models.CharField(max_length=50)),
                ('Total_Mark', models.IntegerField()),
                ('grade', models.CharField(max_length=1)),
                ('comment', models.TextField(max_length=200)),
            ],
        ),
    ]
