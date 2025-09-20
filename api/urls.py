from django.urls import path
from . import views 

urlpatterns = [
    path('students/',views.students),
    path('students/<int:pk>/',views.studentsDetailsView),

    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeesDetailsView.as_view()),
]