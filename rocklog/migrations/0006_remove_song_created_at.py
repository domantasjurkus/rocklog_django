# Generated by Django 3.0.2 on 2020-03-04 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rocklog', '0005_auto_20200304_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='created_at',
        ),
    ]
