from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render


from  Medassistapp.models import Users
from  Medassistapp.serializers import UserSerializer
# from  Medassistapp.serializers import UserGetSerializer

from rest_framework.decorators import api_view

# @api_view(['GET', 'POST', 'DELETE'])
# def Doctors_List(request):
#  if request.method=='GET':
#     doctorlist=Doctors.objects.all()
#     doctor_serializer = DoctorGetSerializer(doctorlist,many=True)
#     return JsonResponse(doctor_serializer.data,safe=False)
#  return JsonResponse({},safe=False) 

@api_view(['GET', 'POST', 'DELETE'])
def Submit_User(request):
  
 try:
   if request.method=='POST':
    User_serializer=UserSerializer(data=request.data)
    # print(doctor_serializer,doctor_serializer.is_valid(),request.data)
    if(User_serializer.is_valid()):
      print("1")
      User_serializer.save()
      return JsonResponse({"message":'User Submitted Successfully',"status":True},safe=False)
    else:
      return JsonResponse({"message":'Fail to  submit User',"status":False},safe=False) 
 except Exception as e:
    print("Error submit:",e)
    return JsonResponse({"message":'Fail to  submit user',"status":False},safe=False) 
 