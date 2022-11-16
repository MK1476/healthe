from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

# Create your views here.
def home(request):
    return render(request, "index.html", {'name': "Nihaal"})

class PatientListView(ListView):
    template_name = "patient/portfolio.html"
    model = models.Patient