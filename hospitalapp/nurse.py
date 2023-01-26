from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Department, Nurse, IpdPatient, OpdPatient
import json
from datetime import datetime

@csrf_exempt
def get_all_nurse(request):
    if (request.method == "GET"):
        #Serialize the data into json
        data = serializers.serialize("json", Nurse.objects.all())
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def get_nurse_by_id(request, id):
    if(request.method == "GET"):
        data = Nurse.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Nurse not found'})
        data = serializers.serialize("json", Nurse.objects.filter(pk=id))
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def create_nurse(request):
    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        dept = Department.objects.get(pk = body['dept_id'])
        date = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        newrecord = Nurse.objects.create(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = date, specialization = body['specialization'], salary=body['salary'], dept_id = dept)
        data = json.loads(serializers.serialize('json', [newrecord]))
        return JsonResponse(data, safe=False)

@csrf_exempt
def delete_nurse(request, id):
    if (request.method == "DELETE"):
        data = Nurse.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Nurse not found'})
        Nurse.objects.filter(pk=id).delete()
        newrecord = Nurse.objects.all()
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

@csrf_exempt
def edit_nurse(request, id):
    if (request.method == "PUT"):
        data = Nurse.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Nurse not found'})
        body = json.loads(request.body.decode("utf-8"))
        dept = Department.objects.get(pk = body['dept_id'])
        date = datetime.strptime(body['date_of_birth'], "%Y-%m-%d").date()
        Nurse.objects.filter(pk=id).update(name=body['name'], contact_no=body['contact_no'], email_id=body['email_id'], date_of_birth = date, specialization = body['specialization'], salary=body['salary'], dept_id = dept)
        newrecord = Nurse.objects.filter(pk=id)
        data = json.loads(serializers.serialize('json', newrecord))
        return JsonResponse(data, safe=False)

@csrf_exempt
def get_all_ipdpatients_of_nurse(request, id):
    if(request.method == "GET"):
        data = Nurse.objects.filter(pk=id)
        if (data.count() == 0):
            return JsonResponse(status=404, data={'message':'Nurse not found'})
        data = serializers.serialize("json", IpdPatient.objects.filter(nurses = id))
        return JsonResponse(json.loads(data), safe=False)