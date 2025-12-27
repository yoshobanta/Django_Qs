from django.urls import path
from teacher.views import *

app_name = "teacher"


urlpatterns = [
    path("result/",result,name="result")
]
