from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    inspect graph json
    """

    verbosity = 1

    def add_arguments(self, parser):

        pass

    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT * FROM refresh_geojson_geometries();
            """)