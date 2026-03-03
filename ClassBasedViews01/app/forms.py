from django import forms
from app.models import *


class SchoolMf(forms.ModelForm):
    class Meta :
        model = School
        fields = '__all__'
        