from django.db import models
from django.utils.timezone import now  

class Appointment(models.Model):
    patient_name = models.CharField(max_length=255, default="Unknown Patient")    
    appointment_date = models.DateTimeField(default=now)
    doctor_name = models.CharField(max_length=255, default="Unknown") 

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"
