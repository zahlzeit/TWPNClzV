# Generated by Django 3.2.5 on 2021-08-18 13:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twpn', '0003_alter_vendor_vendor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='id',
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_email',
            field=models.EmailField(max_length=250),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=100)),
                ('service_price', models.FloatField()),
                ('service_desc', models.CharField(max_length=1000)),
                ('vendor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='twpn.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=250)),
                ('user_serviceDate', models.DateField(default=django.utils.timezone.now,)),
                ('review', models.CharField(max_length=1000)),
                ('vendor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='twpn.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_descName', models.CharField(max_length=100)),
                ('vendor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='twpn.vendor')),
            ],
        ),
    ]
