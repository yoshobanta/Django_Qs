from django import forms

class DeptForm(forms.Form):
    deptnum = forms.IntegerField()
    deptname = forms.CharField()
    deptloc = forms.CharField()
    
class EmpForm(forms.Form):
    pass
    