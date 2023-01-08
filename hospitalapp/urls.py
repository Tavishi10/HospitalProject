from django.urls import path
from . import views
from . import department

urlpatterns = [
    path('department/', department.get_all, name='get_all'),
    path('department/create/', department.create, name='create'),
    path('department/get/<int:id>', department.get_by_id, name='get_by_id'),
    path('department/edit/<int:id>', department.edit, name='edit'),
    path('department/delete/<int:id>', department.delete, name='delete'),
]