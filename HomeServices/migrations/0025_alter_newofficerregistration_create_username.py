# Generated by Django 5.0.4 on 2024-05-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0024_alter_newofficerregistration_create_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newofficerregistration',
            name='Create_username',
            field=models.CharField(max_length=250),
        ),
    ]