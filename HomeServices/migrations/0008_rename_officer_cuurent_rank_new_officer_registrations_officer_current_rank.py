# Generated by Django 5.0.4 on 2024-04-27 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0007_alter_new_officer_registrations_officer_department_of_operations_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_officer_registrations',
            old_name='officer_cuurent_rank',
            new_name='officer_current_rank',
        ),
    ]