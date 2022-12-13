# Generated by Django 4.1 on 2022-12-13 14:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RobotCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('currency', models.CharField(choices=[('INR', 'Indian Rupee'), ('USD', 'US Dollar'), ('EUR', 'Euro')], default='INR', max_length=3)),
                ('manufacturing_date', models.DateTimeField()),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='robot', to='robot.manufacturer')),
                ('robot_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='robot', to='robot.robotcategory')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
