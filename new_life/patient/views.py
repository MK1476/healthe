from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from . import models
from . forms import PatientForm
from new_life.constants import BLOOD_GROUPS, GENDER_CHOICES

# Create your views here.
def home(request):
    return render(request, "index.html", {'name': "Nihaal"})

class PatientListView(ListView):
    template_name = "patient/portfolio.html"
    model = models.Patient

def create(request):
    form = PatientForm()
    error = ""
    
    print(request.method)
    if request.method == 'POST':
        data = request.POST.copy()
        form = PatientForm(data, request.FILES)

        username = data['user_name']
        pw, rep_pw = data['password'], data['repeat_password']
        if pw == rep_pw:
            user, not_created = User.objects.get_or_create(username=username)
            if form.is_valid():
                if not_created:
                    user.set_password(pw)
                
                    patient = form.save(commit=False)
                    patient.user = user

                    patient.save()
                    user.save()
                    return redirect('patient:home')
                    
                else:
                    error = 'User already exists'

            else:
                error = form.errors
        
        else:
            error = "Make sure to enter the same password"

    return render(request, 'patient/forms.html', {'form': form, 'genders': GENDER_CHOICES, 'blood_groups': BLOOD_GROUPS, "error": error})
    
def home(request):
    return render(request, 'index.html', {'name': 'Nihaal'})