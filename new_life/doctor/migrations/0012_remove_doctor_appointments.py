# Generated by Django 4.1.3 on 2022-12-06 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0011_doctor_appointments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="appointments",
        ),
    ]
