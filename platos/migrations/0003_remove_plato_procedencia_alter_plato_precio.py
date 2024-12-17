# Generated by Django 5.1.4 on 2024-12-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0002_plato_procedencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plato',
            name='procedencia',
        ),
        migrations.AlterField(
            model_name='plato',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]