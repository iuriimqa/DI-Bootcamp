from django import forms
from .models import *

class AddRentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'

class AddVehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'