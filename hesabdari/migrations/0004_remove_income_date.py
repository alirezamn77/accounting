# Generated by Django 3.2.5 on 2021-07-21 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hesabdari', '0003_income_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='Date',
        ),
    ]
