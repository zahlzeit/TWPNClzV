# Generated by Django 3.2.5 on 2021-08-22 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twpn', '0010_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
