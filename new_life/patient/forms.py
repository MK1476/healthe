from django import forms
from . models import Patient

class PatientForm(forms.ModelForm):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Patient
        # fields = '__all__'
        exclude = ["user", "registration_date_time"]
            