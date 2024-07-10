from rest_framework import serializers 

from Medassistapp.models import  Doctors


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Doctors
        fields = '__all__'

class DoctorGetSerializer(serializers.ModelSerializer):
    
    class Meta:
       
        model = Doctors
        fields = '__all__'


        
