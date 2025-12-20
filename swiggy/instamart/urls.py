from django.urls import path

from instamart.views import *

app_name = 'instamart'


urlpatterns = [
    path('instamart/',instamart,name='instamart'),
    path('instamart_str/',instamart_str,name='instamart_str')
]