from django.db import models
from .models import Doctor, Nurse, Person

class OpdPatient(Person):
    address = models.CharField(max_length=60)
    gender = models.CharField()
    bill_amount = models.DecimalField(decimal_places=2)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' %(self.name, self.contact_no, self.address, self.gender)

class IpdPatient(Person):
    address = models.CharField(max_length=60)
    gender = models.CharField()
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL)
    nurses = models.ManyToManyField(Nurse)
    ward = models.CharField(max_length=20)
    medicine_charges = models.DecimalField(decimal_places=2, default=0)
    bloodcheck_charges = models.DecimalField(decimal_places=2, default= 0)
    radiology_charges = models.DecimalField(decimal_places=2, default=0)
    injection_charges = models.DecimalField(decimal_places=2, default=0)
    laundary_charges = models.DecimalField(decimal_places=2, default=0)
    misc_charges = models.DecimalField(decimal_places=2, default=0)
    bill_amount = models.DecimalField(decimal_places=2, default=0)
    bill_paid = models.BooleanField(default=False)
    admission_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField()

    def __str__(self):
        return '%s %s %s %s' %(self.name, self.contact_no, self.address, self.gender, self.ward)

