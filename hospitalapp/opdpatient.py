from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Department, Doctor, OpdPatient
import json
from datetime import datetime

@csrf_exempt
def get_all_opdpatient(request):
    if (request.method == "GET"):
        data = serializers.serialize("json", OpdPatient.objects.all())
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def get_opdpatient_by_id(request, id):
    if(request.method == "GET"):
        data = serializers.serialize("json", OpdPatient.objects.filter(pk=id))
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def create_opdpatient(request):
    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        doctor = Doctor.objects.get(pk = body['doctor_id'])
        date = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        newrecord = OpdPatient.objects.create(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = date, address=body['address'], gender=body['gender'], doctor_id = doctor)
        data = json.loads(serializers.serialize('json', [newrecord]))
        return JsonResponse(data, safe=False)

@csrf_exempt
def edit_opdpatient(request, id):
    pass

@csrf_exempt
def delete_opdpatient(request, id):
    if (request.method == "DELETE"):
        OpdPatient.objects.filter(pk=id).delete()
        newrecord = OpdPatient.objects.all()
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)