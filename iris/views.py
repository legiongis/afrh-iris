import os

from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseNotFound


# @permission_required(
#     "doc_viewer.view_docs"
# )  # Replace permission_name with the name of the permission that will be required to view the documentation
def docs_view(request, path):
    mkdocs_path = settings.DOCS_ROOT
    # Check if the documentation exists
    if not os.path.exists(mkdocs_path):
        return HttpResponseNotFound("Documentation does not exist.")

    # If the path is empty, display the home page
    if path == "":
        path = "index.html"

    # Check if the file for the given path exists in the documentation
    file_path = os.path.join(mkdocs_path, path)
    if not os.path.isfile(file_path):
        return HttpResponseNotFound("Page does not exist.")

    # Reading the contents of the file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # If the file is an HTML file, replace relative paths with absolute paths
    if path.endswith(".html"):
        url = request._current_scheme_host
        content = content.replace('"assets/', f'"{url}/media/')
        content = content.replace('"../assets/', f'"{url}/media/')
        content = content.replace('"../../assets/', f'"{url}/media/')
        content = content.replace('"img/', f'"{url}/media/img/')
        content = content.replace('"../img/', f'"{url}/media/img/')
        content = content.replace('"../../img/', f'"{url}/media/img/')

    # Return the contents of the file
    return HttpResponse(content)
