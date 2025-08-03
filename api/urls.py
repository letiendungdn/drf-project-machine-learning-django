from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),  # Assuming you want to handle specific student retrieval or updates
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.Employees.as_view()),
]  