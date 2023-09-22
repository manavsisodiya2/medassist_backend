"""medassist_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Medassistapp import statecity
from Medassistapp import category
from Medassistapp import patient
from Medassistapp import questions
from Medassistapp import subquestions
from Medassistapp import doctor,timings
from django.urls import include, re_path

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^api/statelist', statecity.State_List),
    re_path(r'^api/citylist', statecity.City_List),
    re_path(r'^api/categorylist', category.Category_List),
    re_path(r'^api/doctorsubmit', doctor.Submit_Doctor),
    re_path(r'^api/usersubmit', patient.Submit_Patient),
    re_path(r'^api/doctoredit', doctor.Edit_Doctor),
    re_path(r'^api/doctordelete', doctor.Delete_Doctor),
    re_path(r'^api/doctorpictureedit', doctor.Edit_Picture),
    re_path(r'^api/doctorlist', doctor.Doctors_List),
    re_path(r'^api/edittimings',timings.EditTimings),
    re_path(r'^api/deletetimings',timings.DeleteTimings),
    re_path(r'^api/timingsubmit',timings.TimingSubmit),
    re_path(r'^api/dtiminglist',timings.TimingList),
    re_path(r'^api/questionlist',questions.QuestionList),
    re_path(r'^api/questionsubmit',questions.QuestionSubmit),
    re_path(r'^api/subquestionsubmit',subquestions.SubQuestionsSubmit),



]
