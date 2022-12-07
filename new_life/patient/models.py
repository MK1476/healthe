from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User

from new_life import validators
from new_life.constants import GENDER_CHOICES, BLOOD_GROUPS

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_photo/patient/', blank=True, validators=[validators.validate_file_size])
    date_of_birth = models.DateField()
    phone_number = PhoneNumberField(region="AE", blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    address = models.CharField(max_length=100, blank=True)
    eid = models.CharField(verbose_name="Emirates ID",validators=[validators.phone_regex], blank=False, max_length=18)
    registration_date_time = models.DateTimeField(default=timezone.now, blank=True)
    
    def __str__(self) -> str:
        return self.full_name