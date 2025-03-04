from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def assign_user_group(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name=instance.role)
        instance.groups.add(group)
