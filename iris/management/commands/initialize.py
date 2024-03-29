import json
from pathlib import Path

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management import call_command
from django.core.management.base import BaseCommand

from arches.app.models.models import Concept, MapLayer

class Command(BaseCommand):
    """
    Operations used for initial installation.
    """

    verbosity = 1

    def add_arguments(self, parser):
        parser.add_argument(
            "operation",
            choices=[
                "groups",
                "map-layers",
                "test-users",
            ],
            help="initialization operation to perform"
        )
        parser.add_argument(
            "--undo",
            action="store_true",
        )

    def handle(self, *args, **options):

        self.verbosity = options['verbosity']

        if options['operation'] == "groups":
            self.make_groups()

        if options['operation'] == "test-users":
            self.make_test_users()

        if options['operation'] == "map-layers":
            self.update_default_layer_names(undo=options['undo'])
            self.load_historical_maps()

    def make_groups(self):
        admin1, _ = Group.objects.get_or_create(name="admin1")
        admin2, _ = Group.objects.get_or_create(name="admin2")
        afrh_staff, _ = Group.objects.get_or_create(name="afrh_staff")
        afrh_volunteer, _ = Group.objects.get_or_create(name="afrh_volunteer")
        development, _ = Group.objects.get_or_create(name="development")

        return {
            'admin1': admin1,
            'admin2': admin2,
            'afrh_staff': afrh_staff,
            'afrh_volunteer': afrh_volunteer,
            'development': development,
        }

    def make_test_users(self):

        # a test user will be made for each item in this list.
        # they will be given the same password as their username.
        # they will be added to a group that matches their username,
        # as well as any extra_groups.
        test_users = [
            {
                "username": "admin1",
                "extra_groups": ["RDM Administrator"]
            },
            {
                "username": "admin2",
                "extra_groups": []
            },
            {
                "username": "afrh_staff",
                "extra_groups": []
            },
            {
                "username": "afrh_volunteer",
                "extra_groups": []
            },
            {
                "username": "development",
                "extra_groups": []
            },
        ]

        for user in test_users:
            username = user["username"]
            groups = [username] + user["extra_groups"]

            u, _ = get_user_model().objects.get_or_create(username=username)
            u.set_password(username)
            u.save()

            for group in groups:
                g = Group.objects.get(name=group)
                g.user_set.add(u)

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
