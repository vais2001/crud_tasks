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


#serilization
# def get_number(request,pk):
    # worker=Worker.objects.all()
    # worker=Worker.objects.get(id=pk)
    # print(worker)
    # serializer=WorkerSerializer(worker,many=True)
    # serializer=WorkerSerializer(worker)
    # print(serializer)
    # json_data=JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type="application/json")
    
    # return HttpResponse(serializer.data,content_type="application/json")
    # return JsonResponse(serializer.data,safe=False)




# deserilization
@csrf_exempt
def creation(request):
  if request.method=="POST":
    # request.headers.get('phone_number')
    # print( request.headers.get('phone_number'))
    phone = request.headers.get('phone')
    print(phone)
    print("hhhhhhhhhhhhh")
    json_data=request.body
    print(json_data)
    stream=io.BytesIO(json_data)
    # python_data=json.loads(json_data)
    python_data=JSONParser().parse(stream)
    print(python_data)
    serializer=WorkerSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        res={'msg':'data created'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type="application/json")
    # json_data=JSONRenderer().render(serializer.errors)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse({"msg":"This is not working"})
    