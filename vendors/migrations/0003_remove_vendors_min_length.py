# Generated by Django 2.1.4 on 2019-01-19 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_vendors_min_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendors',
            name='min_length',
        ),
    ]
