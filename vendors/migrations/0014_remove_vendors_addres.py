# Generated by Django 2.1.4 on 2019-01-20 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0013_auto_20190120_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendors',
            name='addres',
        ),
    ]