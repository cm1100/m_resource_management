# tenant_app/models.py

from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        EMPLOYEE = "EMPLOYEE", "Employee"

    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=Role.choices)
    tenant_id = models.IntegerField()

    class Meta:
        unique_together = ('username', 'tenant_id')  # Enforce unique per tenant
        db_table = 'user'

    def save(self, *args, **kwargs):
        # Automatically hash password if it's not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.tenant.name})"




class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    tenant_id = models.IntegerField()

    def __str__(self):
        return self.name


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audit_logs')
    action = models.CharField(max_length=50, choices=[
        ('CREATED_RESOURCE', 'Created Resource'),
        ('UPDATED_RESOURCE', 'Updated Resource'),
        ('DELETED_RESOURCE', 'Deleted Resource'),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.action} - {self.timestamp}"