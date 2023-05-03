from django import forms 
from .models import *

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput()
        }

