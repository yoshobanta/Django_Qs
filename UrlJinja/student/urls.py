from django.urls import path
from student.views import *

app_name = 'student'

urlpatterns = [
    path("rollNum/",rollNum,name="rollNum")
]
