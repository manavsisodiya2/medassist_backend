from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from  Medassistapp.models import States
from  Medassistapp.models import City

 
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
def Edit_Doctor(request):
  
 try:
   if request.method=='POST':
   
      doctors=Doctors.objects.get(pk=request.data['id'])
      
      doctors.category_id=request.data['category']
      doctors.doctorname=request.data['doctorname']
      doctors.gender=request.data['gender']
      doctors.dob=request.data['dob']
      doctors.states_id=request.data['states']
      doctors.city_id=request.data['city']
      doctors.address=request.data['address']
      doctors.qualification=request.data['qualification']
      doctors.emailid=request.data['emailid']
      doctors.mobileno=request.data['mobileno']
      doctors.save()
      return JsonResponse({"message":'Doctor Edited Successfully',"status":True},safe=False)
   
 except Exception as e:
    print("Error edit:",e)
    return JsonResponse({"message":'Fail to  Edit doctor',"status":False},safe=False) 
 
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
  


@api_view(['GET', 'POST', 'DELETE'])
def Edit_Picture(request):
  
 try:
   if request.method=='POST':
      doctors=Doctors.objects.get(pk=request.data['id'])
      doctors.photograph=request.data['photograph']
      doctors.save()
      return JsonResponse({"message":'Doctor Image Edited Successfully',"status":True},safe=False)
   
 except Exception as e:
    print("Error Picture:",e)
    return JsonResponse({"message":'Fail to edit  doctor image',"status":False},safe=False) 
