# Generated by Django 5.1.3 on 2024-11-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('words_found', models.JSONField()),
                ('remaining_time', models.IntegerField()),
            ],
        ),
    ]
