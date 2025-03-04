from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
