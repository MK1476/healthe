from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from new_life import validators, constants

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_photo/patient/', blank=True, validators=[validators.validate_file_size], default='profile_photo/profile_placeholder.jpg')
    category = models.CharField(choices=constants.CATEGORIES, default='P', max_length=1, null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = PhoneNumberField(region="AE", blank=False, null=True)
    gender = models.CharField(max_length=1, choices=constants.GENDER_CHOICES, null=True)
    blood_group = models.CharField(max_length=3, choices=constants.BLOOD_GROUPS, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    eid = models.CharField(verbose_name="Emirates ID",validators=[validators.phone_regex], blank=False, max_length=18, null=True)
    
    def save(self, *args, **kwargs):
        # Combine first_name and last_name to create full_name
        self.full_name = f"{self.first_name} {self.last_name}".strip()
        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
