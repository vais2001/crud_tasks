from django.shortcuts import render
from .models import *
from .serializers import WorkerSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# get name list

def get_data(request):
    if request.method == 'GET':
        try:
            workers = Worker.objects.all()
            print(workers)
            serializer = WorkerSerializer(workers, many=True)
            worker_names = [worker['name'] for worker in serializer.data]
            print(worker_names)
            return JsonResponse(worker_names, safe=False)
        except Exception as e:
            return JsonResponse({'msg': str(e)})

# if we find iexact


def get_data(request):
    if request.method == 'GET':
        try:
            search_name = 'vk'  # The name you're searching for
            worker = Worker.objects.filter(name__iexact=search_name).first()
            print(worker)
            if worker:
                serializer = WorkerSerializer(worker)
                print(serializer)
                worker_name = serializer.data['name'] 
                print(worker_name)
                return JsonResponse({'name': worker_name})
            else:
                return JsonResponse({'msg': f'No worker found with the name "{search_name}".'})
        except Exception as e:
            return JsonResponse({'msg': str(e)})

# CREATION/////////////////////////////
@csrf_exempt
def creation(request):
  if request.method=="POST":
    json_data=request.body
    print(json_data)
    python_data=json.loads(json_data)
    print(python_data)
    serializer=WorkerSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        res={'msg':'data created'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type="application/json")
    return JsonResponse({"msg":"This is not working"})



# UPDATION///////////////////////////

@csrf_exempt
def update_worker(request):
    if request.method == "PUT":
        try:
            json_data = request.body
            print(json_data,type(json_data))
            python_data = json.loads(json_data)
            worker_id=python_data['worker_id']
            worker = Worker.objects.get(worker_id=worker_id)
            # print("0000000000000000000000000000000")
            serializer = WorkerSerializer(worker, data=python_data, partial=True)
            # print(111111111111111111)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data updated'}
                return JsonResponse(res)
            return JsonResponse(serializer.errors, status=400)
        except Worker.DoesNotExist:
            return JsonResponse({'msg': f'Worker with ID {id} not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'msg': str(e)}, status=500)

# DELETE DATA
@csrf_exempt

def delete_data(request):
    if request.method=='POST':
        json_data=request.body
        python_data=json.loads(json_data)
        worker_id=python_data['worker_id']
        worker_id=python_data.get('worker_id')
        worker=Worker.objects.get(worker_id=worker_id)
        print(worker)
        worker.delete()
        return JsonResponse({"deleted":1})
    
    