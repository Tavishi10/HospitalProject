from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Department, Doctor, OpdPatient, IpdPatient
import json
from datetime import datetime

@csrf_exempt
def get_all_doctor(request):
    if (request.method == "GET"):
        data = serializers.serialize("json", Doctor.objects.all())
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def get_doctor_by_id(request, id):
    if(request.method == "GET"):
        data = Doctor.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Doctor not found'})
        dataserialise = serializers.serialize("json", Doctor.objects.filter(pk=id))
        return JsonResponse(json.loads(dataserialise), safe=False)

@csrf_exempt
def create_doctor(request):
    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        dept = Department.objects.get(pk = body['dept_id'])
        date = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        newrecord = Doctor.objects.create(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = date, specialization = body['specialization'], opd_fees = body['opd_fees'], salary=body['salary'], dept_id = dept)
        data = json.loads(serializers.serialize('json', [newrecord]))
        return JsonResponse(data, safe=False)

@csrf_exempt
def delete_doctor(request, id):
    if (request.method == "DELETE"):
        data = Doctor.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Doctor not found'})
        Doctor.objects.filter(pk=id).delete()
        newrecord = Doctor.objects.all()
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

@csrf_exempt
def edit_doctor(request, id):
    if (request.method == "PUT"):
        data = Doctor.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Doctor not found'})
        body = json.loads(request.body.decode("utf-8"))
        dept = Department.objects.get(pk = body['dept_id'])
        date = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        Doctor.objects.filter(pk=id).update(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = date, specialization = body['specialization'], opd_fees = body['opd_fees'], salary=body['salary'], dept_id = dept)
        newrecord = Doctor.objects.filter(pk=id)
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

@csrf_exempt
def get_all_opdpatients_of_doctor(request, id):
    if(request.method == "GET"):
        data = Doctor.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Doctor not found'})
        data = serializers.serialize("json", OpdPatient.objects.filter(doctor_id = id))
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def get_all_ipdpatients_of_doctor(request, id):
    if(request.method == "GET"):
        data = Doctor.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Doctor not found'})
        data = serializers.serialize("json", IpdPatient.objects.filter(doctor_id = id))
        return JsonResponse(json.loads(data), safe=False)

