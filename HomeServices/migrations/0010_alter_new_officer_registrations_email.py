# Generated by Django 5.0.4 on 2024-04-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0009_remove_officer_login_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_officer_registrations',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
    ]
