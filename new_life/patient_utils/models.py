from django.db import models

# Create your models here.
class Lab(models.Model):
    patient = models.ForeignKey('patient.Patient', models.CASCADE)
    doctor = models.ForeignKey('doctor.Doctor', models.CASCADE)
    staff = models.ForeignKey('staff.Staff', models.CASCADE)
    date_of_release = models.DateField()

    def __str__(self) -> str:
        return f'{self.patient} for {self.doctor}'

class XRay(models.Model):
    patient = models.ForeignKey('patient.Patient', models.CASCADE)
    doctor = models.ForeignKey('doctor.Doctor', models.CASCADE)
    staff = models.ForeignKey('staff.Staff', models.CASCADE)
    date_of_release = models.DateField()

    def __str__(self) -> str:
        return f'{self.patient} for {self.doctor}'

class MedicalReport(models.Model):
    patient = models.ForeignKey('patient.Patient', models.CASCADE)
    appointment = models.ForeignKey('appointment.Appointment', models.CASCADE)
    lab = models.ForeignKey('patient_utils.Lab', models.CASCADE)
    xray = models.ForeignKey('patient_utils.XRay', models.CASCADE)
    allergies = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.appointment.__str__()

    
    