from django import forms
from app.models import *


class TopicForms(forms.ModelForm):
    class Meta :
        model = Topic
        fields = '__all__'
    