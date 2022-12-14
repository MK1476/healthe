# Generated by Django 4.1.3 on 2022-12-11 14:05

from django.db import migrations, models
import new_life.validators


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0003_alter_patient_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                default="images/profile_placeholder.jpg",
                upload_to="profile_photo/patient/",
                validators=[new_life.validators.validate_file_size],
            ),
        ),
    ]
