# Generated by Django 3.0.2 on 2020-01-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocklog', '0002_auto_20200109_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
