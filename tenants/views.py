# public/views.py

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Tenant
from .serializers import TenantSerializer

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Tenant deleted"}, status=204)