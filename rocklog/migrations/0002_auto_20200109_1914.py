# Generated by Django 3.0.2 on 2020-01-09 19:14

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('rocklog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='date',
        ),
        migrations.AddField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(default=timezone.now(), editable=False),
            preserve_default=False,
        ),
    ]
