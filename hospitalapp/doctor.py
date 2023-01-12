from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Department, Doctor
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
        data = serializers.serialize("json", Doctor.objects.filter(pk=id))
        return JsonResponse(json.loads(data), safe=False)

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
        Doctor.objects.filter(pk=id).delete()
        newrecord = Doctor.objects.all()
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

@csrf_exempt
def edit_doctor(request, id):
    if (request.method == "PUT"):
        body = json.loads(request.body.decode("utf-8"))
        dept = Department.objects.get(pk = body['dept_id'])
        date = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        Doctor.objects.filter(pk=id).update(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = date, specialization = body['specialization'], opd_fees = body['opd_fees'], salary=body['salary'], dept_id = dept)
        newrecord = Doctor.objects.filter(pk=id)
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)