# Generated by Django 4.0.5 on 2022-06-27 16:09

from django.db import migrations
import users.modelmanagers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.modelmanagers.UserManager()),
            ],
        ),
    ]