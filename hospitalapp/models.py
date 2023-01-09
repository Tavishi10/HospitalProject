from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=30)

    def __str__(self):
        return self.dept_name

class Person(models.Model):
    name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=15)
    email_id = models.EmailField(max_length=20)
    date_of_birth = models.DateField()

    class Meta:
        abstract = True

class Staff(Person):
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' %(self.name, self.contact_no)

class Doctor(Person):
    specialization = models.CharField(max_length=20)
    opd_fees = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' %(self.name, self.contact_no, self.specialization)

class Nurse(Person):
    specialization = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' %(self.name, self.contact_no, self.specialization)

class OpdPatient(Person):
    address = models.CharField(max_length=60)
    gender = models.CharField(max_length=10)
    bill_amount = models.DecimalField(decimal_places=2, max_digits=15)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s %s %s %s' %(self.name, self.contact_no, self.address, self.gender)

class IpdPatient(Person):
    address = models.CharField(max_length=60)
    gender = models.CharField(max_length=10)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    nurses = models.ManyToManyField(Nurse)
    ward = models.CharField(max_length=20)
    medicine_charges = models.DecimalField(decimal_places=2, default=0, max_digits=15)
    bloodcheck_charges = models.DecimalField(decimal_places=2, default= 0, max_digits=15)
    radiology_charges = models.DecimalField(decimal_places=2, default=0, max_digits=15)
    injection_charges = models.DecimalField(decimal_places=2, default=0, max_digits=15)
    laundary_charges = models.DecimalField(decimal_places=2, default=0, max_digits=15)
    misc_charges = models.DecimalField(decimal_places=2, default=0, max_digits=15)
    bill_amount = models.DecimalField(decimal_places=2, default=0, max_digits=15)
    bill_paid = models.BooleanField(default=False)
    admission_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField()

    def __str__(self):
        return '%s %s %s %s' %(self.name, self.contact_no, self.address, self.gender, self.ward)