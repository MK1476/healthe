# Generated by Django 4.1.3 on 2022-12-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0002_alter_appointment_issued_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="room",
            field=models.CharField(max_length=10),
        ),
    ]
