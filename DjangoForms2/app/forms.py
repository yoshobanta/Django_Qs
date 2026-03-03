from django import forms
from app.models import *

class TopicForm(forms.Form):
    topicname = forms.CharField()

class WebpageForm(forms.Form):
    topicname = forms.ModelChoiceField(queryset=Topics.objects.all())
    name = forms.CharField()
    url = forms.URLField()
    
    
class TopicModelForm(forms.ModelForm):
    class Meta :
        model = Topics
        fields = '__all__'
        
class WebpageModelForm(forms.ModelForm):
    class Meta :
        model = Webpage
        fields = '__all__'