from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewSet)

urlpatterns = [
    path('students/',views.students),
    path('students/<int:pk>/',views.studentsDetailsView),

    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeesDetailsView.as_view()),
    path('',include(router.urls))
]