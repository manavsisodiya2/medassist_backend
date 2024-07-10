from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render


 
from  Medassistapp.models import Doctors
from  Medassistapp.serializers import DoctorSerializer
from  Medassistapp.serializers import DoctorGetSerializer



from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def Doctors_List(request):
 if request.method=='GET':
    doctorlist=Doctors.objects.all()
    doctor_serializer = DoctorGetSerializer(doctorlist,many=True)
    return JsonResponse(doctor_serializer.data,safe=False)
 return JsonResponse({},safe=False) 


@api_view(['GET', 'POST', 'DELETE'])
def Submit_Doctor(request):
  
 try:
   if request.method=='POST':
    doctor_serializer=DoctorSerializer(data=request.data)
    # print(doctor_serializer,doctor_serializer.is_valid(),request.data)
    if(doctor_serializer.is_valid()):
    
      doctor_serializer.save()
      return JsonResponse({"message":'Doctor Submitted Successfully',"status":True},safe=False)
    else:
      return JsonResponse({"message":'Fail to  submit doctor',"status":False},safe=False) 
 except Exception as e:
    print("Error submit:",e)
    return JsonResponse({"message":'Fail to  submit doctor',"status":False},safe=False) 
 

@api_view(['GET', 'POST', 'DELETE'])
def Delete_Doctor(request):
  
 try:
   if request.method=='POST':
      print(request.data)
      doctors=Doctors.objects.get(pk=request.data['id'])
      doctors.delete()
      return JsonResponse({"message":'Doctor Deleted Successfully',"status":True},safe=False)
   
 except Exception as e:
    print("Error delete:",e)
    return JsonResponse({"message":'Fail to Delete submit doctor',"status":False},safe=False) 
  


