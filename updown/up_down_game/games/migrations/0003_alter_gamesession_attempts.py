# Generated by Django 4.2.16 on 2024-11-08 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_gamesession_user_guess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesession',
            name='attempts',
            field=models.IntegerField(default=0),
        ),
    ]