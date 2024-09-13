from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from datetime import date
import re

# Create your models here.
def validate_letters(value):
    if not re.match ("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError('Name must contain only letters.')
    return value


class Passenger(models.Model):
    full_name = models.CharField(max_length=50,null=False, validators=[MinLengthValidator(3),validate_letters])
    gender = models.CharField(null=False, max_length=50)
    date_of_birth = models.DateField(null=False,)
    nationality = models.CharField(null=False,max_length=50,default=False)
    phone_number = models.CharField(null=False,max_length=50)
    email_address = models.CharField(null=False,max_length=50)
    P_O_box_number = models.CharField(null=False,max_length=50) 
    emergency_phone_number = models.CharField(max_length=225, null=False)
    passport_number = models.CharField(max_length=30,default=False,null=False)
    visa_document = models.FileField(upload_to='cvs/')
    departure_city = models.CharField(max_length=50,default=False,null=False)
    destination_city = models.CharField(max_length=50)


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def str(self):
        return self.full_name