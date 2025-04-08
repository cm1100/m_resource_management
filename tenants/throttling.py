from rest_framework.throttling import SimpleRateThrottle

class TenantTokenRateThrottle(SimpleRateThrottle):
    def get_cache_key(self, request, view):

        tenant_id = getattr(request.user_data, 'tenant_id', None)
        if not tenant_id:
            return None

        return self.cache_format % {
            'scope': 'tenant',
            'ident': str(tenant_id),
        }

    def get_rate(self):
        # Set the rate here instead of using scope
        return '1/min'  # You can make this dynamic based on tenant if needed
