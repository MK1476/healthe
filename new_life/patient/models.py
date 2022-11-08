from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = PhoneNumberField(region="AE", blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    phone_regex = RegexValidator(regex=r"^(\d{1,3}(-(\d{1,4}(-(\d{1,7}(-(\d{1,1})?)?)?)?)?)?)$", message="Emirates ID must be in format 111-1111-1111111-1")
    eid = models.CharField(verbose_name="Emirates ID",validators=[phone_regex], blank=False, max_length=18)
    registration_date_time = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self) -> str:
        return self.name