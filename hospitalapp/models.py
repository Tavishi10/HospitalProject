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