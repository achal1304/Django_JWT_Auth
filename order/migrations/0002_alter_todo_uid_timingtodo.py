# Generated by Django 4.1 on 2022-11-09 15:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a89a71b0-c86a-4738-be07-efab0a4ccda3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TimingTodo',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('a89a71b0-c86a-4738-be07-efab0a4ccda3'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('timing', models.DateField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
