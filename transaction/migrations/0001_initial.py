# Generated by Django 4.2.1 on 2023-05-09 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=13)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sum', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
