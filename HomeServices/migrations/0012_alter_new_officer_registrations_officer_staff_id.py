# Generated by Django 5.0.4 on 2024-04-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0011_alter_new_officer_registrations_phone_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_officer_registrations',
            name='officer_staff_ID',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
