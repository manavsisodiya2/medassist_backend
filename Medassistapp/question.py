from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from  Medassistapp.models import Questions
from  Medassistapp.models import SubQuestions
from  Medassistapp.serializers import QuestionSerializer
from  Medassistapp.serializers import SubQuestionSerializer

from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def Question_List(request):
  if request.method=='POST':
  
    id=request.data['id']
    
    questionlist=Questions.objects.all().filter(category_id=id)
     
    question_serializer = QuestionSerializer(questionlist,many=True)
  
    return JsonResponse(question_serializer.data,safe=False)
  return JsonResponse({},safe=False)  