import datetime

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Resource, AuditLog, User



@receiver(post_save, sender=Resource)
def log_resource_update(sender, instance, created, **kwargs):
    action="CREATED_RESOURCE"
    if not created:
        action = 'UPDATED_RESOURCE'
    user = instance.owner
    AuditLog.objects.create(
        user=user,
        action=action,
        timestamp=datetime.datetime.now()
    )

@receiver(post_delete, sender=Resource)
def log_resource_deletion(sender, instance, **kwargs):
    action = 'DELETED_RESOURCE'
    user = instance.owner
    AuditLog.objects.create(
        user=user,
        action=action,
        timestamp=datetime.datetime.now()
    )