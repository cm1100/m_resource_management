from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import connection
from .models import Tenant  # your tenant model

@receiver(post_delete, sender=Tenant)
def delete_tenant_schema(sender, instance, **kwargs):
    schema_name = instance.schema_name
    if schema_name and schema_name != 'public':
        with connection.cursor() as cursor:
            cursor.execute(f'DROP SCHEMA IF EXISTS "{schema_name}" CASCADE;')
