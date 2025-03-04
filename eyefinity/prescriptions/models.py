from django.db import models
from patients.models import Patient
from inventory.models import InventoryItem

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.first_name} {self.patient.last_name}"

class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="items")
    medicine = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.medicine.name} - {self.dosage}"
