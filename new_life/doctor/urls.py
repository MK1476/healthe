from django.urls import path
from . import views

app_name = 'doctor'
urlpatterns = [
    path('create', views.create, name='create'),
    path('new', views.home, name='new')
]
