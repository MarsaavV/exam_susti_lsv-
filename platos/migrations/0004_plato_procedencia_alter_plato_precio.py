# Generated by Django 5.1.4 on 2024-12-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0003_remove_plato_procedencia_alter_plato_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='procedencia',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plato',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
