# Generated by Django 4.1.3 on 2022-11-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapl', '0004_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='nombre',
            field=models.CharField(default='desconocidoo', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(default='desconocidoo', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(default='desconocidoo', max_length=30, unique=True),
        ),
    ]