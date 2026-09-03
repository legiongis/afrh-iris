from arches.settings_utils import generate_frontend_configuration
from django.apps import AppConfig
from django.conf import settings


class AfrhPrjConfig(AppConfig):
    name = "afrh_prj"
    is_arches_application = True

    def ready(self):
        if settings.APP_NAME.lower() == self.name:
            generate_frontend_configuration()
