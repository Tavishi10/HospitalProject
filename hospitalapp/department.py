from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Department
import json

@csrf_exempt
def get_all(request):
    if (request.method == "GET"):
        #Serialize the data into json
        data = serializers.serialize("json", Department.objects.all())
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def create(request):
    if (request.method == "POST"):
        # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        #create the new item
        newrecord = Department.objects.create(dept_name=body['dept_name'])
        # Turn the object to json to dict, put in array to avoid non-iterable error
        data = json.loads(serializers.serialize('json', [newrecord]))
        # send json response with new object
        return JsonResponse(data, safe=False)
    
@csrf_exempt
def get_by_id(request, id):
    if(request.method == "GET"):
        data = serializers.serialize("json", Department.objects.filter(pk=id))
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def edit(request, id):
    if (request.method == "PUT"):
        # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        # update the item
        Department.objects.filter(pk=id).update(dept_name=body['dept_name'])
        newrecord = Department.objects.filter(pk=id)
        # Turn the object to json to dict, put in array to avoid non-iterable error
        data = json.loads(serializers.serialize('json', newrecord))
        # send json response with updated object
        return JsonResponse(data, safe=False)

@csrf_exempt
def delete(request, id):
    if (request.method == "DELETE"):
        # delete the item, get all remaining records for response
        Department.objects.filter(pk=id).delete()
        newrecord = Department.objects.all()
        # Turn the results to json to dict, put in array to avoid non-iterable error
        data = json.loads(serializers.serialize('json', newrecord))
        # send json response with updated object
        return JsonResponse(data, safe=False)


