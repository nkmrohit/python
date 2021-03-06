# Generated by Django 2.1.4 on 2019-01-25 03:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('mname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('address', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
