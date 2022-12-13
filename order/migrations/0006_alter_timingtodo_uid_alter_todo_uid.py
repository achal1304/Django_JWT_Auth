# Generated by Django 4.1 on 2022-12-13 14:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_timingtodo_uid_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('172a76d7-7726-4063-b466-1010ca9db5b7'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('172a76d7-7726-4063-b466-1010ca9db5b7'), editable=False, primary_key=True, serialize=False),
        ),
    ]