from django.urls import path
from . import views

app_name = 'appointment'
urlpatterns = [
    path("create", views.create, name="create"),
    path('ajax/load-doctors/', views.load_doctors, name='ajax_load_doctors'), # AJAX
    path('ajax/load-slots/', views.time_slots, name='ajax_load_slots'), # AJAX
]
