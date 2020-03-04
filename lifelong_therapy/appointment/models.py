import datetime

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Therapist(models.Model):
    therapist_name = models.CharField(max_length = 40)
    therapist_email = models.EmailField(default="unspecified@foo.com", max_length = 40)

    def __str__(self):
        return self.therapist_name

class Patient(models.Model):
    patient_name = models.CharField(max_length = 40)
    patient_email = models.EmailField(default="unspecified@foo.com", max_length = 40)
    patient_phone_number = models.CharField(max_length = 10, blank = True) # TODO consider using regex in future 
    '''in UK numbers are formatted like this;
    +44 7911 123456 global
    0 7911 123456 local
    '''
    appointment_date = models.DateField()
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name

    def is_appointment_date_near(self):
        return self.appointment_date <= timezone.now() + datetime.timedelta(days = 3)

