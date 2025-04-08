# tenant_app/views.py
from django.db.models.signals import post_save
from rest_framework import viewsets
from .models import User,Resource, AuditLog
from .serializers import UserSerializer,ResourceSerializer, AuditLogSerializer
from tenants.throttling import TenantTokenRateThrottle

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    throttle_classes = [TenantTokenRateThrottle]

    def perform_update(self, serializer):
        # Save the object first
        instance = serializer.save()
        return instance
        # Manually trigger the post_save signal for the updated resource
        #post_save.send(sender=Resource, instance=instance, created=False)


class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    throttle_classes = [TenantTokenRateThrottle]