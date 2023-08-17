from rest_framework import serializers
from .models import *



# class WorkerSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=255)
#     phone_number=serializers.CharField(max_length=255)



# deserilizatin
class WorkerSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=255)
    phone_number=serializers.CharField(max_length=255)
    
#     # class Meta:
#     #     model = Worker
#     #     fields = ('name', 'phone_number')
    
    
    def create(self,validate_data):
        return Worker.objects.create(**validate_data)
    

# # UPDATION
    def update(self,instance,validate_data):
        # instance.name=validate_data.get('name',instance.name)
        instance.phone_number=validate_data.get('phone_number',instance.phone_number)
        instance.save()
        return instance