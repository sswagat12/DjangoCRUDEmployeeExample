from django.urls import path
from . import views
  
urlpatterns = [
      path('', views.employees_crud, name = 'home'),
      path('create', views.add_employee, name='create_employee'),
      path('all', views.view_all_employees, name = 'retrieve_employees'),
      path('update/<int:pk>', views.update_employee, name = 'update_employee'),
      path('delete/<int:pk>', views.delete_employee, name = 'delete_employee')
]