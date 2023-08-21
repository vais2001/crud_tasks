from rest_framework import serializers
from .models import *



class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Worker
        fields = '__all__'

    def create(self,validate_data):
        return Worker.objects.create(**validate_data)
    

# # UPDATION
    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.phone_number=validate_data.get('phone_number',instance.phone_number)
        instance.address=validate_data.get('address',instance.address)
        instance.save()
        return instance