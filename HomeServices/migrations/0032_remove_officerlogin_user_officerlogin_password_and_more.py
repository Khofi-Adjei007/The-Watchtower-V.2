# Generated by Django 5.0.4 on 2024-05-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0031_remove_officerlogin_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officerlogin',
            name='user',
        ),
        migrations.AddField(
            model_name='officerlogin',
            name='password',
            field=models.CharField(default=128, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='officerlogin',
            name='username',
            field=models.CharField(default=250, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
