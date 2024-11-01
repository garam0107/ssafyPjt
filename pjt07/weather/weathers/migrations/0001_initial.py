# Generated by Django 4.2.16 on 2024-11-01 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_txt', models.DateField()),
                ('temp', models.FloatField()),
                ('feels_like', models.FloatField()),
            ],
        ),
    ]
