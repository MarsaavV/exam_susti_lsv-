# Generated by Django 5.1.4 on 2024-12-15 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesero',
            name='dni',
            field=models.IntegerField(default=0),
        ),
    ]