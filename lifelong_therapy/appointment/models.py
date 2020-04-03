import datetime
import pytz

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Therapist(models.Model):
    therapist_name = models.CharField(max_length = 40)
    therapist_email = models.EmailField(default="unspecified@foo.com", max_length = 40)
    therapist_time_schedule = [datetime.time(i,0,0) for i in range(9,17)]

    def __str__(self):
        return self.therapist_name

class Patient(models.Model):
    patient_name = models.CharField(max_length = 40)
    patient_email = models.EmailField(default="unspecified@foo.com", max_length = 40)
    patient_phone_number = models.CharField(max_length = 10, blank = True) 
    # TODO consider using regex in future for only UK numbers
    # TODO consider adding text message to the patients phone in UK 
    '''in UK numbers are formatted like this;
    +44 7911 123456 global
    0 7911 123456 local
    '''
    # tzinfo=pytz.timezone("Europe/London")
    # p = Patient(patient_name="patient pelia", patient_phone_number="404",appointment_date=datetime.datetime(2020,1,1,15,0,0,tzinfo=pytz.UTC), therapist=t) 
    appointment_date = models.DateTimeField("date appointed")
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name

    def is_appointment_date_near(self):
        return self.appointment_date <= timezone.now() + datetime.timedelta(days = 3)

