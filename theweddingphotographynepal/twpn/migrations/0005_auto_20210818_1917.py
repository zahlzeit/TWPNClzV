# Generated by Django 3.2.5 on 2021-08-18 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twpn', '0004_auto_20210818_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='user_serviceDate',
            field=models.DateField(),
        ),
    ]
