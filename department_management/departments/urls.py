from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),  # List of departments
    path('create/', views.department_create, name='department_create'),  # Create a new department
    path('update/<int:dept_id>/', views.department_update, name='department_update'),  # Update an existing department
    path('delete/<int:dept_id>/', views.department_delete, name='department_delete'),  # Delete a department
]
