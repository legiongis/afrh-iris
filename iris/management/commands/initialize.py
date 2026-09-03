
from arches.app.models.models import MapLayer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Operations used for initial installation.
    """

    verbosity = 1

    def add_arguments(self, parser):
        parser.add_argument(
            "operation",
            choices=[
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

        if options['operation'] == "test-users":
            self.make_test_users()

        if options['operation'] == "map-layers":
            self.update_default_layer_names(undo=options['undo'])
            self.load_historical_maps()

    def make_test_users(self):

        # a test user will be made for each item in this list.
        # they will be given the same password as their username.
        # they will be added to a group that matches their username,
        # as well as any extra_groups.
        test_users = [
            {
                "username": "admin1",
                "groups": [
                    "Admin 1",
                ]
            },
            {
                "username": "admin2",
                "groups": [
                    "Admin 2",
                ]
            },
            {
                "username": "afrh_staff",
                "groups": [
                    "AFRH Staff",
                ]
            },
            {
                "username": "afrh_volunteer",
                "groups": [
                    "AFRH Volunteer",
                ]
            },
            {
                "username": "plc_staff",
                "groups": [
                    "PLC Staff",
                ]
            },
            {
                "username": "contractor",
                "groups": [
                    "Contractor",
                ]
            },
        ]

        for user in test_users:
            username = user["username"]

            u, _ = get_user_model().objects.get_or_create(username=username)
            u.set_password(username)
            u.save()

            for group in user["groups"]:
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
