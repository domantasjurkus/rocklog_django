# Generated by Django 3.0.3 on 2020-04-06 00:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocklog', '0012_remove_savedsong_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamentry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 0, 26, 26, 537546)),
        ),
    ]