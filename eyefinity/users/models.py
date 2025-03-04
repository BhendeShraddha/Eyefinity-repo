from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('receptionist', 'Receptionist'),
        ('patient', 'Patient'),
    )

    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="customuser_users_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="customuser_users_permissions_set",
        blank=True
    )

    def __str__(self):
        return self.username
