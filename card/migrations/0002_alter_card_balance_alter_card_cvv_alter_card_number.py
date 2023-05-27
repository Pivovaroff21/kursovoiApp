# Generated by Django 4.2.1 on 2023-05-10 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='balance',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='card',
            name='cvv',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999999)]),
        ),
    ]