# Generated by Django 4.1 on 2022-12-13 13:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_timingtodo_uid_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4b8c7d36-c60a-4162-aad9-df7a3d3df3c9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4b8c7d36-c60a-4162-aad9-df7a3d3df3c9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
