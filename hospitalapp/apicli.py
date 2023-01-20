import typer
import requests
import json
from django.urls import resolve, reverse

ip = "192.168.64.2"
port = "30159"

app = typer.Typer()

#commands to operate on department
@app.command()
def get_all_departments():
    response = requests.get(f"http://{ip}:{port}/hospital/department/")
    #print(reverse('hospital:get_all_department'))
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def get_department_by_id(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/department/get/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def create_department(dept_name: str):
    response = requests.post(f"http://{ip}:{port}/hospital/department/create/", json={"dept_name": dept_name})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def update_department(id:int , dept_name: str):
    response = requests.put(f"http://{ip}:{port}/hospital/department/edit/{id}", json={"dept_name": dept_name})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def delete_department(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/department/delete/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))


# commands to operate on staff
@app.command()
def get_all_staff():
    response = requests.get(f"http://{ip}:{port}/hospital/staff/")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def get_staff_by_id(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/staff/get/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def create_staff(name: str, contact_no: str, email: str, dob: str, salary: float, dept_id: int):
    response = requests.post(f"http://{ip}:{port}/hospital/staff/create/", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "salary": salary, "dept_id" : dept_id})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def update_staff(id: int, name: str, contact_no: str, email: str, dob: str, salary: float, dept_id: int):
    response = requests.put(f"http://{ip}:{port}/hospital/staff/edit/{id}", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "salary": salary, "dept_id" : dept_id})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def delete_staff(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/staff/delete/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

# commands to operate on nurse
###############################

@app.command()
def get_all_nurses():
    response = requests.get(f"http://{ip}:{port}/hospital/nurse/")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def get_nurse_by_id(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/nurse/get/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def create_nurse(name: str, contact_no: str, email: str, dob: str, spec: str, salary: float, dept_id: int):
    response = requests.post(f"http://{ip}:{port}/hospital/nurse/create/", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "specialization" : spec, "salary": salary, "dept_id" : dept_id})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def update_nurse(id:int, name: str, contact_no: str, email: str, dob: str, spec: str, salary: float, dept_id: int):
    response = requests.put(f"http://{ip}:{port}/hospital/nurse/edit/{id}", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "specialization" : spec, "salary": salary, "dept_id" : dept_id})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def delete_nurse(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/nurse/delete/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))


# # commands to operate on doctor
# ###############################

@app.command()
def get_all_doctors():
    response = requests.get(f"http://{ip}:{port}/hospital/doctor/")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def get_doctor_by_id(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/doctor/get/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def create_doctor(name: str, contact_no: str, email: str, dob: str, spec: str, fees: float, salary: float, dept_id: int):
    response = requests.post(f"http://{ip}:{port}/hospital/doctor/create/", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "specialization" : spec, "opd_fees" : fees, "salary": salary, "dept_id" : dept_id})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def update_doctor(id: int, name: str, contact_no: str, email: str, dob: str, spec: str, fees: float, salary: float, dept_id: int):
    response = requests.put(f"http://{ip}:{port}/hospital/doctor/edit/{id}", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "specialization" : spec, "opd_fees" : fees, "salary": salary, "dept_id" : dept_id})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def delete_doctor(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/doctor/delete/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

# # commands to operate on opdpatient
# ###################################

@app.command()
def get_all_opdpatients():
    response = requests.get(f"http://{ip}:{port}/hospital/opdpatient/")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def get_opdpatient_by_id(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/opdpatient/get/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def create_opdpatient(name: str, contact_no: str, email: str, dob: str, address: str, gender: str, doc_id: int):
    response = requests.post(f"http://{ip}:{port}/hospital/opdpatient/create/", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "address" : address, "gender" : gender, "doc_id" : doc_id})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def update_opdpatient(id : int, name: str, contact_no: str, email: str, dob: str, address: str, gender: str, doc_id: int):
    response = requests.put(f"http://{ip}:{port}/hospital/opdpatient/edit/{id}", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "address" : address, "gender" : gender, "doc_id" : doc_id})
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def delete_opdpatient(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/opdpatient/delete/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

# # commands to operate on ipdpatient
# ###################################

@app.command()
def get_all_ipdpatients():
    response = requests.get(f"http://{ip}:{port}/hospital/ipdpatient/")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

@app.command()
def get_ipdpatient_by_id(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/ipdpatient/get/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))

# @app.command()
# def create_ipdpatient(name: str, contact_no: str, email: str, dob: str, address: str, gender: str, doc_id: int, ward: str, nurses: list):
#     response = requests.post(f"http://{ip}:{port}/hospital/ipdpatient/create/", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "address" : address, "gender" : gender, "doctor_id": doc_id, "ward" : ward, "nurses": nurses})
#     formatted_response = json.loads(response.text)
#     print(json.dumps(formatted_response, indent=2))

# @app.command()
# def update_ipdpatient(id : int, name: str, contact_no: str, email: str, dob: str, address: str, gender: str, doc_id: int, ward: str, nurses: list):
#     response = requests.put(f"http://{ip}:{port}/hospital/ipdpatient/edit/{id}", json={"name" : name, "contact_no" : contact_no, "email_id" : email, "date_of_birth" : dob, "address" : address, "gender" : gender, "doctor_id": doc_id, "ward" : ward, "nurses": nurses})
#     formatted_response = json.loads(response.text)
#     print(json.dumps(formatted_response, indent=2))

@app.command()
def delete_ipdpatient(id: int):
    response = requests.get(f"http://{ip}:{port}/hospital/ipdpatient/delete/{id}")
    formatted_response = json.loads(response.text)
    print(json.dumps(formatted_response, indent=2))


if __name__ == "__main__":
    app()