from rest_framework import serializers
from .models import *
# class WorkerSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=255)
#     phone_number=serializers.CharField(max_length=255)



# deserilizatino
class WorkerSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    phone_number=serializers.CharField(max_length=255)
    
    class Meta:
        model = Worker
        fields = ('name', 'phone_number')
    
    
def create(self,validate_data):
    return Worker.objects.create(**validate_data)
    

