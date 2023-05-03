from django import forms
from .models import *
from crispy_forms.helper import FormHelper


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = 'title','release_date','created_in_country','available_in_countries','category','director'
        widgets = {'title':forms.TextInput(), 'release_date':forms.DateInput(),'created_in_country':forms.Select(),'available_in_countries':forms.SelectMultiple(),'category':forms.SelectMultiple(),'director':forms.SelectMultiple()}

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
