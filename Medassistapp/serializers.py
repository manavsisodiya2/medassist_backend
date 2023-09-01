from rest_framework import serializers 
from Medassistapp.models import  Category
from Medassistapp.models import  States
from Medassistapp.models import  City
from Medassistapp.models import  Doctors
from Medassistapp.models import Timings
class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = "__all__"
class StateSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = States
        fields = "__all__"
class CitySerializer(serializers.ModelSerializer):        
    class Meta:
        model = City
        fields = "__all__"    
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Doctors
        fields = '__all__'

class DoctorGetSerializer(serializers.ModelSerializer):
    states = StateSerializer(many=False)
    city=CitySerializer(many=False)
    category=CategorySerializer(many=False)
    class Meta:
       
        model = Doctors
        fields = '__all__'


        
class TimingsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Timings
        fields = '__all__'                    
class TimingsGetSerializer(serializers.ModelSerializer):
    doctor=DoctorSerializer(many=False)
    class Meta:
        model = Timings
        fields= "__all__"