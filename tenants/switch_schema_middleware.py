import threading
from django.db import connection
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
import jwt
from django.conf import settings

from .models import Tenant  # Make sure to import your Tenant model

class SchemaMiddleware(MiddlewareMixin):
    def process_request(self, request):

        if 'tenant/' in request.path:
            return None

        tenant_id = request.headers.get('TENANT-ID')
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                token = auth_header.split(' ')[1]

                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

                request.user_data = decoded_token
                tenant_id = decoded_token['tenant_id']


            except jwt.ExpiredSignatureError:
                return JsonResponse({'detail': 'Token has expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'detail': 'Invalid token'}, status=401)
            except Exception as e:
                print(e)
                return JsonResponse({'detail': 'Invalid Token'}, status=401)

        schema_name = self.get_schema_from_request(tenant_id)
        self.set_schema(schema_name)

    def process_response(self, request, response):

        self.reset_schema_to_public()
        return response

    def get_schema_from_request(self, tenant_id):



        tenant = Tenant.objects.get(pk=tenant_id)
        return tenant.schema_name

    def set_schema(self, schema_name):

        with connection.cursor() as cursor:
            cursor.execute(f'SET search_path TO {schema_name}, public;')

    def reset_schema_to_public(self):

        with connection.cursor() as cursor:
            cursor.execute('SET search_path TO public;')
