from django.db import models

class Therapist(models.Model):
    therapist_name = models.CharField(max_length = 40)

    def __str__(self):
        return self.author_name

class Patient(models.Model):
    patient_name = models.CharField(max_length = 40)
    appointment_date = models.DateField()
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name



