# Generated by Django 5.1.2 on 2024-10-31 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.TextField(default='normal'),
        ),
    ]
