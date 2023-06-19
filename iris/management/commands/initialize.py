import json
from pathlib import Path

from django.core.management import call_command
from django.core.management.base import BaseCommand

from arches.app.models.models import Concept, MapLayer

class Command(BaseCommand):
    """
    inspect graph json
    """

    verbosity = 1

    def add_arguments(self, parser):

        parser.add_argument(
            "--undo",
            action="store_true",
            help="individual JSON file to inspect"
        )

    def handle(self, *args, **options):

        self.verbosity = options['verbosity']

        self.update_default_layer_names(undo=options['undo'])
        self.load_historical_maps()

    def update_default_layer_names(self, undo=False):

        if undo is False:
            for ml in MapLayer.objects.all():
                if ml.name == "streets":
                    ml.name = "Streets"
                    ml.save()
                if ml.name == "satellite":
                    ml.name = "Aerial Imagery"
                    ml.save()

        else:
            for ml in MapLayer.objects.all():
                if ml.name == "Streets":
                    ml.name = "streets"
                    ml.save()
                if ml.name == "Aerial Imagery":
                    ml.name = "satellite"
                    ml.save()

    def load_historical_maps(self):

        call_command('loaddata', 'historic-map-overlays')
