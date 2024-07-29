# Generated by Django 3.2.5 on 2021-08-21 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('number', models.IntegerField()),
                ('room', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
