# Generated by Django 2.1.4 on 2019-01-27 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerauth', '0003_remove_customers_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='image',
        ),
        migrations.AddField(
            model_name='customers',
            name='address',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
