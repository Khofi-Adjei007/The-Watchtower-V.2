# Generated by Django 5.0.4 on 2024-05-01 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0015_alter_new_officer_registrations_officer_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewOfficerRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('phone_contact', models.IntegerField(unique=True)),
                ('officer_address', models.CharField(max_length=250)),
                ('officer_current_rank', models.CharField(max_length=250)),
                ('officer_current_station', models.CharField(max_length=250)),
                ('officer_staff_ID', models.CharField(max_length=250, unique=True)),
                ('officer_qualification', models.CharField(choices=[('WS', 'WASSCE'), ('DG', 'DEGREE'), ('MS', 'MASTERS'), ('PH', 'PHD')], max_length=2)),
                ('officer_date_of_birth', models.DateField()),
                ('officer_operations_region', models.CharField(max_length=250)),
                ('officer_operations_department', models.CharField(max_length=250)),
                ('officer_profile_image', models.ImageField(upload_to='')),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OfficerLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officer_staff_ID', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='new_officer_registrations',
        ),
        migrations.DeleteModel(
            name='officer_login',
        ),
    ]