import unittest
from django.test import TestCase, Client, SimpleTestCase
from hospitalapp.models import Department, Nurse, Doctor, Staff, OpdPatient, IpdPatient
from datetime import date

class TestDepartmentView(TestCase):
    def setUp(self):
        self.client = Client()

        for i in range(5):
            Department.objects.create(dept_name="ER")

    def test_get_all_departments(self):
        response = self.client.get('/hospital/department/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

    def test_get_department_by_id(self):
        response = self.client.get('/hospital/department/get/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
    
    def test_create_department(self):
        self.assertEqual(Department.objects.all().count(), 5)
        response = self.client.post('/hospital/department/create/', {'dept_name' : 'ENT'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['fields']['dept_name'], "ENT")
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(Department.objects.all().count(), 6)

    def test_update_department(self):
        self.assertEqual(Department.objects.get(pk=1).dept_name, "ER")
        response = self.client.put('/hospital/department/edit/1', {'dept_name' : 'Paramedics'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['fields']['dept_name'], "Paramedics")
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(Department.objects.get(pk=1).dept_name, "Paramedics")

    def test_delete_department(self):
        self.assertEqual(Department.objects.all().count(), 5)
        response = self.client.delete('/hospital/department/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(Department.objects.all().count(), 4)

class TestDoctorView(TestCase):
    def setUp(self):
        self.client = Client()
        dept = Department.objects.create(dept_name="ER")

        for i in range(5):
            Doctor.objects.create(name="Tavishi Suvarna", contact_no="9834758493", email_id="ts@gmail.com", date_of_birth = "1995-5-23", specialization = "Physician", opd_fees = 100, salary=60000, dept_id = dept)

    def test_get_all_doctors(self):
        response = self.client.get('/hospital/doctor/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

    def test_get_doctor_by_id(self):
        response = self.client.get('/hospital/doctor/get/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_create_doctor(self):
        self.assertEqual(Doctor.objects.all().count(), 5)
        response = self.client.post('/hospital/doctor/create/', {"name" : "Ruchita Moon", "contact_no" : "9894959685", "email_id" : "rm@gmail.com", "date_of_birth" : "1995-9-23", "specialization" : "Physician", "opd_fees" : 200, "salary": 65000, "dept_id" : 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(Doctor.objects.all().count(), 6)

    def test_update_doctor(self):
        self.assertEqual(Doctor.objects.get(pk=1).salary, 60000)
        response = self.client.put('/hospital/doctor/edit/1', { "name":"Tavishi Suvarna", "contact_no":"9834758493", "email_id":"ts@gmail.com", "date_of_birth" : "1995-5-23", "specialization" : "Physician", "opd_fees" : 100, "salary":75000, "dept_id" : 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(Doctor.objects.get(pk=1).salary, 75000)

    def test_delete_doctor(self):
        self.assertEqual(Doctor.objects.all().count(), 5)
        response = self.client.delete('/hospital/doctor/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(Doctor.objects.all().count(), 4)
    
class TestNurseView(TestCase):
    def setUp(self):
        self.client = Client()

        dept = Department.objects.create(dept_name="ER")

        for i in range(5):
            Nurse.objects.create(name="Sneha Lahariya", contact_no="9834758493", email_id="sl@gmail.com", date_of_birth = "1995-5-23", specialization = "General", salary=60000, dept_id = dept)

    def test_get_all_nurses(self):
        response = self.client.get('/hospital/nurse/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

    def test_get_nurse_by_id(self):
        response = self.client.get('/hospital/nurse/get/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
    
    def test_create_nurse(self):
        self.assertEqual(Nurse.objects.all().count(), 5)
        response = self.client.post('/hospital/nurse/create/', {"name" : "Madhura Rajhans", "contact_no" : "9894959685", "email_id" : "mr@gmail.com", "date_of_birth" : "1996-9-23", "specialization" : "General", "salary": 65000, "dept_id" : 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(Nurse.objects.all().count(), 6)

    def test_update_nurse(self):
        self.assertEqual(Nurse.objects.get(pk=1).salary, 60000)
        response = self.client.put('/hospital/nurse/edit/1', {"name" : "Sneha Lahariya", "contact_no" : "9834758493", "email_id" : "sl@gmail.com", "date_of_birth" : "1995-5-23", "specialization" : "General", "salary": 75000, "dept_id" : 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(Nurse.objects.get(pk=1).salary, 75000)

    def test_delete_nurse(self):
        self.assertEqual(Nurse.objects.all().count(), 5)
        response = self.client.delete('/hospital/nurse/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Nurse.objects.all().count(), 4)

class TestStaffView(TestCase):
    def setUp(self):
        self.client = Client()
        dept = Department.objects.create(dept_name="Staff")

        for i in range(5):
            Staff.objects.create(name="Sneha Lahariya", contact_no="9834758493", email_id="sl@gmail.com", date_of_birth = "1995-5-23", salary=60000, dept_id = dept)

    def test_get_all_staffs(self):
        response = self.client.get('/hospital/staff/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

    def test_get_staff_by_id(self):
        response = self.client.get('/hospital/staff/get/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_create_staff(self):
        self.assertEqual(Staff.objects.all().count(), 5)
        response = self.client.post('/hospital/staff/create/', {"name" : "Yash Bhange", "contact_no" : "9894959685", "email_id" : "yb@gmail.com", "date_of_birth" : "1993-9-23", "salary": 45000, "dept_id" : 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(Staff.objects.all().count(), 6)

    def test_update_staff(self):
        self.assertEqual(Staff.objects.get(pk=1).salary, 60000)
        response = self.client.put('/hospital/staff/edit/1', {"name" : "Sneha Lahariya", "contact_no" : "9834758493", "email_id" : "sl@gmail.com", "date_of_birth" : "1995-5-23", "salary": 75000, "dept_id" : 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(Staff.objects.get(pk=1).salary, 75000)

    def test_delete_staff(self):
        self.assertEqual(Staff.objects.all().count(), 5)
        response = self.client.delete('/hospital/staff/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(Staff.objects.all().count(), 4)
    
class TestOpdPatientView(TestCase):
    def setUp(self):
        self.client = Client()
        dept = Department.objects.create(dept_name="ER")
        doctor = Doctor.objects.create(name="Tavishi Suvarna", contact_no="9834758493", email_id="ts@gmail.com", date_of_birth = "1995-5-23", specialization = "Physician", opd_fees = 100, salary=60000, dept_id = dept)

        for i in range(5):
            OpdPatient.objects.create(name="Shubham Patil", contact_no="9834758493", email_id="sp@gmail.com", date_of_birth = "1995-5-23", address="Thane", gender="male", doctor_id = doctor)


    def test_get_all_opdpatients(self):
        response = self.client.get('/hospital/opdpatient/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)
    
    def test_get_opdpatient_by_id(self):
        response = self.client.get('/hospital/opdpatient/get/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_create_opdpatient(self):
        self.assertEqual(OpdPatient.objects.all().count(), 5)
        response = self.client.post('/hospital/opdpatient/create/', {"name" : "Yash Bhange", "contact_no" : "9894959685", "email_id" : "yb@gmail.com", "date_of_birth" : "1993-9-23", "address" : "Dombivli", "gender" : "male", "doctor_id" : 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(OpdPatient.objects.all().count(), 6)

    # def test_update_opdpatient(self):
    #     self.assertEqual(OpdPatient.objects.get(pk=1).address, "Thane")
    #     response = self.client.put('/hospital/opdpatient/edit/1', {"name" : "Shubham Patil", "contact_no" : "9894959685", "email_id" : "sp@gmail.com", "date_of_birth" : "1995-5-23", "address" : "Dombivli", "gender" : "male", "doctor_id" : 1}, content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json()), 1)
    #     self.assertEqual(OpdPatient.objects.get(pk=1).address, "Dombivli")

    def test_delete_opdpatient(self):
        self.assertEqual(OpdPatient.objects.all().count(), 5)
        response = self.client.delete('/hospital/opdpatient/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(OpdPatient.objects.all().count(), 4)
    
class TestIpdPatientView(TestCase):
    def setUp(self):
        self.client = Client()
        dept = Department.objects.create(dept_name="ER")
        doctor = Doctor.objects.create(name="Tavishi Suvarna", contact_no="9834758493", email_id="ts@gmail.com", date_of_birth = "1995-5-23", specialization = "Physician", opd_fees = 100, salary=60000, dept_id = dept)

        for i in range(5):
            IpdPatient.objects.create(name="Shubham Patil", contact_no="9834758493", email_id="sp@gmail.com", date_of_birth = "1995-5-23", address="Thane", gender="male", doctor_id = doctor, ward="general", discharge_date = "2023-1-15")


    def test_get_all_ipdpatients(self):
        response = self.client.get('/hospital/ipdpatient/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

    def test_get_ipdpatient_by_id(self):
        response = self.client.get('/hospital/ipdpatient/get/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_create_ipdpatient(self):
        self.assertEqual(IpdPatient.objects.all().count(), 5)
        response = self.client.post('/hospital/ipdpatient/create/', {"name" : "Prakash Singh", "contact_no" : "9894999685", "email_id" : "ps@gmail.com", "date_of_birth" : "1993-9-20", "address" : "Thane", "gender" : "male", "doctor_id" : 1, "ward":"General"}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(IpdPatient.objects.all().count(), 6)

    # def test_update_ipdpatient(self):
    #     self.assertEqual(IpdPatient.objects.get(pk=1).address, "Thane")
    #     response = self.client.put('/hospital/ipdpatient/edit/1', {"name" : "Shubham Patil", "contact_no" : "9894959685", "email_id" : "sp@gmail.com", "date_of_birth" : "1995-5-23", "address" : "Dombivli", "gender" : "male", "doctor_id" : 1, ward="general", discharge_date = "2023-1-15"}, content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json()), 1)
    #     self.assertEqual(IpdPatient.objects.get(pk=1).address, "Dombivli")

    def test_delete_ipdpatient(self):
        self.assertEqual(IpdPatient.objects.all().count(), 5)
        response = self.client.delete('/hospital/ipdpatient/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(IpdPatient.objects.all().count(), 4)
