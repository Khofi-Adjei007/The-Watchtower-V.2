# Generated by Django 5.0.4 on 2024-04-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0006_new_officer_registrations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_officer_registrations',
            name='officer_department_of_operations',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='new_officer_registrations',
            name='officer_staff_ID',
            field=models.CharField(max_length=250),
        ),
    ]
