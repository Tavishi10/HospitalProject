from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Department, Doctor, IpdPatient, Nurse
import json
from datetime import datetime, date

@csrf_exempt
def get_all_ipdpatient(request):
    if (request.method == "GET"):
        data = serializers.serialize("json", IpdPatient.objects.all())
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def get_ipdpatient_by_id(request, id):
    if(request.method == "GET"):
        data = IpdPatient.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Ipd Patient not found'})
        data = serializers.serialize("json", IpdPatient.objects.filter(pk=id))
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def create_ipdpatient(request):
    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        doctor = Doctor.objects.get(pk = body['doctor_id'])
        dob = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        nurses = body['nurses']
        newrecord = IpdPatient.objects.create(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = dob, address=body['address'], gender=body['gender'], doctor_id = doctor, ward=body['ward'], discharge_date = datetime.now().date())
        for i in nurses:
            newrecord.nurses.set(Nurse.objects.filter(pk=i))
        data = json.loads(serializers.serialize('json', [newrecord]))
        return JsonResponse(data, safe=False)

@csrf_exempt
def edit_ipdpatient(request, id):
    if (request.method == "PUT"):
        data = IpdPatient.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Ipd Patient not found'})
        body = json.loads(request.body.decode("utf-8"))
        doctor = Doctor.objects.get(pk = body['doctor_id'])
        dob = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        IpdPatient.objects.filter(pk=id).update(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = dob, address=body['address'], gender=body['gender'], doctor_id = doctor, ward=body['ward'])
        newrecord = IpdPatient.objects.get(pk=id)
        for i in body['nurses']:
            newrecord.nurses.set(Nurse.objects.filter(pk=i))
        data = json.loads(serializers.serialize('json', IpdPatient.objects.filter(pk=id)))
        return JsonResponse(data, safe=False)

@csrf_exempt
def delete_ipdpatient(request, id):
    if (request.method == "DELETE"):
        data = IpdPatient.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Ipd Patient not found'})
        IpdPatient.objects.filter(pk=id).delete()
        newrecord = IpdPatient.objects.all()
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

@csrf_exempt
def update_charges(request, id):
    if(request.method == "PUT"):
        data = IpdPatient.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Ipd Patient not found'})
        body = json.loads(request.body.decode("utf-8"))
        IpdPatient.objects.filter(pk=id).update(bloodcheck_charges=body['bloodcheck_charges'], medicine_charges=body['medicine_charges'], radiology_charges=body['radiology_charges'], laundary_charges=body['laundary_charges'], injection_charges=body['injection_charges'], misc_charges=body['misc_charges'])
        newrecord = IpdPatient.objects.filter(pk=id)
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

@csrf_exempt
def total_bill_amount(request, id):
    if(request.method == "GET"):
        data = IpdPatient.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Ipd Patient not found'})
        patient = IpdPatient.objects.get(pk=id)
        total_amt = patient.bloodcheck_charges + patient.medicine_charges + patient.radiology_charges + patient.laundary_charges + patient.injection_charges + patient.misc_charges
        IpdPatient.objects.filter(pk=id).update(bill_amount= total_amt)
        data = json.loads(serializers.serialize('json', IpdPatient.objects.filter(pk=id)))
        return JsonResponse(data, safe=False)

@csrf_exempt
def discharge(request, id):
    if(request.method == "PUT"):
        data = IpdPatient.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Ipd Patient not found'})
        body = json.loads(request.body.decode("utf-8"))
        date = datetime.strptime(body['discharge_date'], "%Y-%m-%d").date()
        IpdPatient.objects.filter(pk=id).update(bill_paid=body['bill_paid'], discharge_date=date)
        data = json.loads(serializers.serialize('json', IpdPatient.objects.filter(pk=id)))
        return JsonResponse(data, safe=False)




