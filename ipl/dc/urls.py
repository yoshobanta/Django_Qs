from django.urls import path
from dc.views import *

app_name = 'something'

urlpatterns = [
    path('captain', captain , name='captain'),
    path('vice_captain',vice_captain,name="vice_captain")
]