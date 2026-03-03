from django import forms

#normal function validator . only one element can be pass i.e value.
#Can we perform email validation using this ?
def check_age(value):
    if value < 18 :
        raise forms.ValidationError('Invalid age')
    

class ContactForm(forms.Form):
    name = forms.CharField()    #no validation as nothing inside CharFiled( Here no validation ) so everything will pass
    age = forms.IntegerField(validators=[check_age])  #Normal fun validator connected here .
    email = forms.EmailField()
    reemail = forms.EmailField()
    botcatcher = forms.CharField(widget=forms.HiddenInput,required=False)
    

    #clean_element - use for bot catcher . and url inputs not user inputs through forms but inputs from url .
    def clean_botcatcher(self):
        a = self.cleaned_data['botcatcher']
        if len(a)>0:
            raise forms.ValidationError('Botcatcher caught')

    
    #clean
    def clean(self):
        e = self.cleaned_data['email']
        re = self.cleaned_data['reemail']
        
        if e != re :
            raise forms.ValidationError('Email is not same a Re-Enter Email')  #This will not show . in older version of django it is showing .
        
        
    