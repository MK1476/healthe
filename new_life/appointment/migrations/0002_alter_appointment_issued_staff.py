# Generated by Django 4.1.3 on 2022-12-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0003_staff_user"),
        ("appointment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="issued_staff",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="staff.staff",
            ),
        ),
    ]