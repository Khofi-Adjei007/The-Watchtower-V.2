# Generated by Django 5.0.4 on 2024-05-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0033_delete_officerlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficerLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
