from django import forms
from django.forms import ModelForm
from FP_App.models import *

class First_form(forms.Form):
    name = forms.CharField()
    email     = forms.EmailField()
    # company_name = forms.CharField()
    phone     = forms.CharField()
    subject   = forms.CharField()
    message   = forms.CharField()

class Secondform(ModelForm):
    class Meta:
        model= Contact
        fields=('__all__')  

    
