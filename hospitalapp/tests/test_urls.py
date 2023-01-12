from django.test import SimpleTestCase, Client
from django.urls import resolve, reverse
from hospitalapp.department import get_all, get_by_id, create_department, delete_department, edit_department
from hospitalapp.staff import get_all_staff, get_staff_by_id, create_staff, delete_staff, edit_staff
from hospitalapp.nurse import get_all_nurse, get_nurse_by_id, create_nurse, delete_nurse, edit_nurse
from hospitalapp.doctor import get_all_doctor, get_doctor_by_id, create_doctor, edit_doctor, delete_doctor
from hospitalapp.opdpatient import get_all_opdpatient, get_opdpatient_by_id, create_opdpatient, edit_opdpatient, delete_opdpatient
from hospitalapp.ipdpatient import get_all_ipdpatient, get_ipdpatient_by_id, create_ipdpatient, edit_ipdpatient, delete_ipdpatient

class TestDepartmentUrls(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_department_url_is_resolved(self):
        url = reverse('get_all_department')
        self.assertAlmostEquals(resolve(url).func, get_all)

    def test_get_department_by_id_url_is_resolved(self):
        url = reverse('get_department_by_id', args=[1])
        self.assertAlmostEquals(resolve(url).func, get_by_id)

    def test_create_department_url_is_resolved(self):
        url = reverse('create_department')
        self.assertAlmostEquals(resolve(url).func, create_department)

    def test_edit_department_url_is_resolved(self):
        url = reverse('edit_department', args=[1])
        self.assertAlmostEquals(resolve(url).func, edit_department)

    def test_delete_department_url_is_resolved(self):
        url = reverse('delete_department', args=[1])
        self.assertAlmostEquals(resolve(url).func, delete_department)

class TestStaffUrls(SimpleTestCase):
    def setUp(self):
        self.client = Client()    

    def test_get_all_staff_url_is_resolved(self):
        url = reverse('get_all_staff')
        self.assertAlmostEquals(resolve(url).func, get_all_staff)

    def test_get_staff_by_id_url_is_resolved(self):
        url = reverse('get_staff_by_id', args=[1])
        self.assertAlmostEquals(resolve(url).func, get_staff_by_id)

    def test_create_staff_url_is_resolved(self):
        url = reverse('create_staff')
        self.assertAlmostEquals(resolve(url).func, create_staff)

    def test_edit_staff_url_is_resolved(self):
        url = reverse('edit_staff', args=[1])
        self.assertAlmostEquals(resolve(url).func, edit_staff)

    def test_delete_staff_url_is_resolved(self):
        url = reverse('delete_staff', args=[1])
        self.assertAlmostEquals(resolve(url).func, delete_staff)

class TestNurseUrls(SimpleTestCase):
    def setUp(self):
        self.client = Client()    

    def test_get_all_nurse_url_is_resolved(self):
        url = reverse('get_all_nurse')
        self.assertAlmostEquals(resolve(url).func, get_all_nurse)

    def test_get_nurse_by_id_url_is_resolved(self):
        url = reverse('get_nurse_by_id', args=[1])
        self.assertAlmostEquals(resolve(url).func, get_nurse_by_id)

    def test_create_nurse_url_is_resolved(self):
        url = reverse('create_nurse')
        self.assertAlmostEquals(resolve(url).func, create_nurse)

    def test_edit_nurse_url_is_resolved(self):
        url = reverse('edit_nurse', args=[1])
        self.assertAlmostEquals(resolve(url).func, edit_nurse)

    def test_delete_nurse_url_is_resolved(self):
        url = reverse('delete_nurse', args=[1])
        self.assertAlmostEquals(resolve(url).func, delete_nurse)

class TestDoctorUrls(SimpleTestCase):
    def setUp(self):
        self.client = Client()    

    def test_get_all_doctor_url_is_resolved(self):
        url = reverse('get_all_doctor')
        self.assertAlmostEquals(resolve(url).func, get_all_doctor)

    def test_get_doctor_by_id_url_is_resolved(self):
        url = reverse('get_doctor_by_id', args=[1])
        self.assertAlmostEquals(resolve(url).func, get_doctor_by_id)

    def test_create_doctor_url_is_resolved(self):
        url = reverse('create_doctor')
        self.assertAlmostEquals(resolve(url).func, create_doctor)

    def test_edit_doctor_url_is_resolved(self):
        url = reverse('edit_doctor', args=[1])
        self.assertAlmostEquals(resolve(url).func, edit_doctor)

    def test_delete_doctor_url_is_resolved(self):
        url = reverse('delete_doctor', args=[1])
        self.assertAlmostEquals(resolve(url).func, delete_doctor)

class TestOpdPatientUrls(SimpleTestCase):
    def setUp(self):
        self.client = Client()    

    def test_get_all_opdpatient_url_is_resolved(self):
        url = reverse('get_all_opdpatient')
        self.assertAlmostEquals(resolve(url).func, get_all_opdpatient)

    def test_get_opdpatient_by_id_url_is_resolved(self):
        url = reverse('get_opdpatient_by_id', args=[1])
        self.assertAlmostEquals(resolve(url).func, get_opdpatient_by_id)

    def test_create_opdpatient_url_is_resolved(self):
        url = reverse('create_opdpatient')
        self.assertAlmostEquals(resolve(url).func, create_opdpatient)

    def test_edit_opdpatient_url_is_resolved(self):
        url = reverse('edit_opdpatient', args=[1])
        self.assertAlmostEquals(resolve(url).func, edit_opdpatient)

    def test_delete_opdpatient_url_is_resolved(self):
        url = reverse('delete_opdpatient', args=[1])
        self.assertAlmostEquals(resolve(url).func, delete_opdpatient)

class TestIpdPatientUrls(SimpleTestCase):
    def setUp(self):
        self.client = Client()    

    def test_get_all_ipdpatient_url_is_resolved(self):
        url = reverse('get_all_ipdpatient')
        self.assertAlmostEquals(resolve(url).func, get_all_ipdpatient)

    def test_get_ipdpatient_by_id_url_is_resolved(self):
        url = reverse('get_ipdpatient_by_id', args=[1])
        self.assertAlmostEquals(resolve(url).func, get_ipdpatient_by_id)

    def test_create_ipdpatient_url_is_resolved(self):
        url = reverse('create_ipdpatient')
        self.assertAlmostEquals(resolve(url).func, create_ipdpatient)

    def test_edit_ipdpatient_url_is_resolved(self):
        url = reverse('edit_ipdpatient', args=[1])
        self.assertAlmostEquals(resolve(url).func, edit_ipdpatient)

    def test_delete_ipdpatient_url_is_resolved(self):
        url = reverse('delete_ipdpatient', args=[1])
        self.assertAlmostEquals(resolve(url).func, delete_ipdpatient)
        
