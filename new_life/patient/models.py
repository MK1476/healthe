from django.db import models

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField('user_profile.UserProfile', models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'