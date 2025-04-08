from django.core.management import BaseCommand

from tenants.models import Tenant
from tenants.utils import create_schema_and_migrate


class Command(BaseCommand):


    def handle(self, *args, **options):

        print("started")
        schema_name = Tenant.objects.get(pk=6).schema_name

        create_schema_and_migrate(schema_name)