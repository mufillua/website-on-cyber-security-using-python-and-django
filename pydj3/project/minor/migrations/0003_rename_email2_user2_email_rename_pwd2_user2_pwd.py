# Generated by Django 4.0.6 on 2022-11-15 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0002_user2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user2',
            old_name='email2',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user2',
            old_name='pwd2',
            new_name='pwd',
        ),
    ]
