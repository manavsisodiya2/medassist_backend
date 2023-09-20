from rest_framework import serializers 
from Medassistapp.models import  Category
from Medassistapp.models import  Questions
from Medassistapp.models import  SubQuestions
from Medassistapp.models import  States
from Medassistapp.models import  City
from Medassistapp.models import  Doctors
from Medassistapp.models import  Timings
from Medassistapp.models import  Patient
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

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Questions
        fields = "__all__"
class SubQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= SubQuestions
        fields = "__all__"
        
class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Patient
        fields="__all__"