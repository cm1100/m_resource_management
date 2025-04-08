import subprocess

from django.core.management import call_command
from django.db import connection
import os

def create_schema_and_migrate(schema_name):

    with connection.cursor() as cursor:
        cursor.execute(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"')


    with connection.cursor() as cursor:
        cursor.execute(f'SET search_path TO {schema_name}')

    call_command('migrate')


