# Generated by Django 4.1.3 on 2023-09-16 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="blood_group",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="date_of_birth",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="eid",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="email",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="full_name",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="profile_pic",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="registration_date_time",
        ),
    ]