from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

from new_life import validators
from new_life.constants import GENDER_CHOICES, BLOOD_GROUPS, WORKING_HOURS

# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_photo/staff/', blank=True, validators=[validators.validate_file_size])
    date_of_birth = models.DateField()
    phone_number = PhoneNumberField(region="AE", blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    department = models.ForeignKey('department.Department', models.CASCADE)
    eid = models.CharField(verbose_name="Emirates ID",validators=[validators.phone_regex], blank=False, max_length=18)
    registration_date_time = models.DateTimeField(default=timezone.now, blank=True)
    working_hours = models.CharField(choices=WORKING_HOURS, max_length=11)
    role = models.ForeignKey('staff.Role', models.CASCADE)

    def __str__(self) -> str:
        return self.full_name

class Role(models.Model):
    name = models.CharField(max_length=25)
    number_of_staff = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.name