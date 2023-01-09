from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Department, Staff
import json
from datetime import datetime

@csrf_exempt
def get_all_staff(request):
    if (request.method == "GET"):
        data = serializers.serialize("json", Staff.objects.all())
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def get_staff_by_id(request, id):
    if(request.method == "GET"):
        data = serializers.serialize("json", Staff.objects.filter(pk=id))
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def create(request):
    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        dept = Department.objects.get(pk = body['dept_id'])
        date = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        newrecord = Staff.objects.create(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = date, salary=body['salary'], dept_id = dept)
        data = json.loads(serializers.serialize('json', [newrecord]))
        return JsonResponse(data, safe=False)

@csrf_exempt
def delete(request, id):
    if (request.method == "DELETE"):
        Staff.objects.filter(pk=id).delete()
        newrecord = Staff.objects.all()
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

@csrf_exempt
def edit(request, id):
    if (request.method == "PUT"):
        body = json.loads(request.body.decode("utf-8"))
        dept = Department.objects.get(pk = body['dept_id'])
        date = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        Staff.objects.filter(pk=id).update(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = date, salary=body['salary'], dept_id = dept)
        newrecord = Staff.objects.filter(pk=id)
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)