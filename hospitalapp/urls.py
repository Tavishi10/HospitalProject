from django.urls import path
from . import department, nurse, staff, doctor, opdpatient, ipdpatient

urlpatterns = [
    path('department/', department.get_all, name='get_all'),
    path('department/create/', department.create, name='create'),
    path('department/get/<int:id>', department.get_by_id, name='get_by_id'),
    path('department/edit/<int:id>', department.edit, name='edit'),
    path('department/delete/<int:id>', department.delete, name='delete'),
    path('staff/', staff.get_all_staff, name='get_all_staff'),
    path('staff/create/', staff.create, name='create'),
    path('staff/get/<int:id>', staff.get_staff_by_id, name='get_staff_by_id'),
    path('staff/edit/<int:id>', staff.edit, name='edit'),
    path('staff/delete/<int:id>', staff.delete, name='delete'),
    path('nurse/', nurse.get_all_nurse, name='get_all_nurse'),
    path('nurse/create/', nurse.create, name='create'),
    path('nurse/get/<int:id>', nurse.get_nurse_by_id, name='get_nurse_by_id'),
    path('nurse/edit/<int:id>', nurse.edit, name='edit'),
    path('nurse/delete/<int:id>', nurse.delete, name='delete'),
    path('doctor/', doctor.get_all_doctor, name='get_all_doctor'),
    path('doctor/create/', doctor.create, name='create'),
    path('doctor/get/<int:id>', doctor.get_doctor_by_id, name='get_doctor_by_id'),
    path('doctor/edit/<int:id>', doctor.edit, name='edit'),
    path('doctor/delete/<int:id>', doctor.delete, name='delete'),
    path('opdpatient/', opdpatient.get_all_opdpatient, name='get_all_opdpatient'),
    path('opdpatient/create/', opdpatient.create_opdpatient, name='create_opdpatient'),
    path('opdpatient/get/<int:id>', opdpatient.get_opdpatient_by_id, name='get_opdpatient_by_id'),
    path('opdpatient/edit/<int:id>', opdpatient.edit_opdpatient, name='edit_opdpatient'),
    path('opdpatient/delete/<int:id>', opdpatient.delete_record, name='delete_record'),
    path('ipdpatient/', ipdpatient.get_all_ipdpatient, name='get_all_ipdpatient'),
    path('ipdpatient/create/', ipdpatient.create_ipdpatient, name='create_ipdpatient'),
    path('ipdpatient/get/<int:id>', ipdpatient.get_ipdpatient_by_id, name='get_ipdpatient_by_id'),
    path('ipdpatient/edit/<int:id>', ipdpatient.edit_ipdpatient, name='edit_ipdpatient'),
    path('ipdpatient/delete/<int:id>', ipdpatient.delete_record, name='delete_record'),
]