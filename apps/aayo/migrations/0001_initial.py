# Generated by Django 5.0.7 on 2024-08-02 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('menu', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_link', models.CharField(max_length=255, unique=True)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aayo.cafe')),
            ],
        ),
        migrations.CreateModel(
            name='RoomAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('session_key', models.CharField(max_length=255)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aayo.room')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_menu', models.CharField(max_length=255)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aayo.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aayo.roomaccount')),
            ],
        ),
    ]
