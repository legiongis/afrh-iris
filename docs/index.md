# Overview

These docs will provide a comprehensive description of the AFRH-IRIS code base, and how to work with it. For more about how to work with Arches in general, see the [official documentation](https://arches.readthedocs.io). Currently, AFRH-IRIS is built from Arches v6.2

## Organization

The AFRH-IRIS code base is organized as follows:

- **`afrh_prj/`** - This is the Arches **project**, and it holds the main application logic and settings.
    - see [Project Customizations](/docs/package)
    - see [Understanding Projects](https://arches.readthedocs.io/en/stable/installing/projects-and-packages/) in the Arches documentation for more context.
- **`pkg/`** - This is the Arches **package**, it holds database models, thesauri, and other configurations used during installation.
    - see [Package Content](/docs/project)
    - see [Understanding Packages](https://arches.readthedocs.io/en/stable/installing/projects-and-packages/#understanding-packages) in the Arches documentation for more context.
- **`iris/`** - This is a custom Django app that holds a few management commands and fixtures.
    - see [Management Commands](/docs/management) and [Custom Map Layers](/docs/map-layers)
- **`docs/`** - This is a mkdocs documentation module that holds this documentation.
    - see [Building the Docs](/docs/documentation)

## Clean install

A `clean_install.sh` script is included that will perform the following:

- create a new database using the credentials supplied in `settings.py`
- load the package
- load local business_data (this is not committed to the repository)
- run the `initialize` management command (see [Management Commands](/docs/management))

Run this with

    source ./clean_install.sh

!!! Warning
    This will drop and recreate your database (full data loss).

## Building the Docs

This documentation is built with [mkdocs-material](https://squidfunk.github.io/mkdocs-material). The markdown content is stored in **`docs/`**, and it is configured to build into **`.docs/`** (which is gitignored). A view in the `iris` app passes built docs content to the proper urls.

Use `mkdocs serve -a localhost:8001` to view the docs in a browser during development.

Use `mkdocs build` to regenerate the static docs pages that will be served to the AFRH-IRIS frontend.