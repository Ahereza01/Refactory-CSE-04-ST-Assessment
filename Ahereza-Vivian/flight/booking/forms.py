from django import forms
from django.core.exceptions import ValidationError
from .models import Passenger

class BookingForm(forms.ModelForm):
    gender = [
        ('Male','Male'),
        ('Female','Female')
    ]

    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    gender = forms.ChoiceField(choices=gender, required=False, widget=forms.Select(attrs={'class': 'form-control','placeholder': '--select--'}))

    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'placeholder': 'dd-mm-yyyy'}))

    nationality = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    email_address = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    P_O_box_number = forms.IntegerField(widget=forms.NumberInput(), required=False)

    emergency_phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    passport_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    visa_Document = forms.FileField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'upload file'}))

    departure_city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    destination_city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

   

    class Meta:
        model = Passenger
        fields = '__all__'