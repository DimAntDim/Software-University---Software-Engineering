from django import forms
from .models import Profile

class FormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    

class FormCreateProfile(FormProfile):
    pass

