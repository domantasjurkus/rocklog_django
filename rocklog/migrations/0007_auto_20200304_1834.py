# Generated by Django 3.0.2 on 2020-03-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocklog', '0006_remove_song_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
