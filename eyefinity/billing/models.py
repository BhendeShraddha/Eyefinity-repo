from django.db import models
from users.models import CustomUser
from appointments.models import Appointment

class Invoice(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="invoices")
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.patient.username} - {self.status}"
