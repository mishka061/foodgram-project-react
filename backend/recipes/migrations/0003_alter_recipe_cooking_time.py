# Generated by Django 4.1.7 on 2023-03-17 13:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1, message='За минуту даже на индукции не готовится.')], verbose_name='Время приготовления'),
        ),
    ]
