from django.db import models
from tenants.utils import create_schema_and_migrate


class Tenant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    schema_name = models.CharField(max_length=63, unique=True)

    class Meta:
        db_table = 'tenant'

    def __str__(self):
        return f"{self.name} ({self.schema_name})"


    def save(
        self,
        *args,
        **kwargs,
    ):
        res=super().save(*args,**kwargs)
        create_schema_and_migrate(self.schema_name)
        return res
