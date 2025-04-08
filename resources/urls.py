# tenant_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,ResourceViewSet,AuditLogViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'auditlogs', AuditLogViewSet)

urlpatterns = [
    path('view_set/', include(router.urls)),
]
