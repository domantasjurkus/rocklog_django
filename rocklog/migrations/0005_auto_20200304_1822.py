# Generated by Django 3.0.2 on 2020-03-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocklog', '0004_auto_20200110_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='date',
            field=models.DateTimeField(editable=False),
        ),
    ]
