from django.urls import path
from patient.views import home, PatientListView

urlpatterns = [
    path("home", PatientListView.as_view(), name="home")
]
