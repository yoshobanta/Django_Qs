from django.urls import path
from food.views import *

app_name = 'food'


urlpatterns = [
    path('food/',food,name='food'),
    path('food_str/',food_str,name='food_str')
]