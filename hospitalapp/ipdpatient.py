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
        data = serializers.serialize("json", IpdPatient.objects.filter(pk=id))
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def create_ipdpatient(request):
    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        doctor = Doctor.objects.get(pk = body['doctor_id'])
        dob = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        newrecord = IpdPatient.objects.create(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = dob, address=body['address'], gender=body['gender'], doctor_id = doctor, ward=body['ward'], discharge_date = date.today)
        data = json.loads(serializers.serialize('json', [newrecord]))
        return JsonResponse(data, safe=False)

@csrf_exempt
def edit_ipdpatient(request, id):
    pass

@csrf_exempt
def delete_record(request, id):
    if (request.method == "DELETE"):
        IpdPatient.objects.filter(pk=id).delete()
        newrecord = IpdPatient.objects.all()
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

