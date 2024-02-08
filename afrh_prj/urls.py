from django.conf.urls import include, url, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from iris.views import docs_view

urlpatterns = [
    url(r'^', include('arches.urls')),
    re_path(r"^docs/(?P<path>.*)$", docs_view, name="docs"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.SHOW_LANGUAGE_SWITCH is True:
    urlpatterns = i18n_patterns(*urlpatterns)
