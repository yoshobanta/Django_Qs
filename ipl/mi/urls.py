from django.urls import path
from mi.views import *

app_name = 'anything'


urlpatterns = [
    path('captain/',captain,name='captain')
]