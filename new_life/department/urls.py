from django.urls import path
from . import views

app_name = 'department'
urlpatterns = [
    path("", views.DepartmentListView.as_view(), name="list"),
    path("<int:pk>", views.DepartmentDetailView.as_view(), name="detail")
]
