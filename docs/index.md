# Overview

These docs will provide a comprehensive description of the AFRH-IRIS code base, and how to work with it. For more about how to work with Arches in general, see the [official documentation](https://arches.readthedocs.io). Currently, AFRH-IRIS is built from Arches v6.2.

## Organization

The AFRH-IRIS code base is organized as follows:

- **`afrh_prj/`** - This is the Arches **project**, and it holds the main application logic and settings.
    - see [Project Customizations](/docs/package.html)
    - see [Understanding Projects](https://arches.readthedocs.io/en/stable/installing/projects-and-packages/) in the Arches documentation for more context.
- **`pkg/`** - This is the Arches **package**, it holds database models, thesauri, and other configurations used during installation.
    - see [Package Content](/docs/project.html)
    - see [Understanding Packages](https://arches.readthedocs.io/en/stable/installing/projects-and-packages/#understanding-packages) in the Arches documentation for more context.
- **`iris/`** - This is a custom Django app that holds a few management commands and fixtures.
    - see [Management Commands](/docs/management.html) and [Custom Map Layers](/docs/map-layers.html)
- **`docs/`** - This is a mkdocs documentation module that holds this documentation.
    - see [Building the Docs](#building-the-docs)

## Clean install

A `clean_install.sh` script is included that will perform the following:

- create a new database using the credentials supplied in `settings.py`
- create the AFRH-IRIS user groups that will be used for permissions
- load the package
- load local business_data (this data is not committed to the repository)
- update some map layer configs and load historical map overlays

Run this with

    source ./clean_install.sh

!!! Warning
    This will drop and recreate your database (full data loss).

To create a set of test user accounts, one per permissions level, use

    python manage.py initialize test-users

See [permissions > Test Accounts](/docs/permissions.html#test-accounts) > Test Accounts to learn more about these accounts (and permissions in general).

The `initialize` command is also used within the clean install script. For more on that command, see [Management Commands](/docs/management.html).

!!! Warning
    Arches does not support the load of resource model-level permissions from packages. This means that most of the permissions described.

## Building the Docs

This documentation is built with [mkdocs-material](https://squidfunk.github.io/mkdocs-material). The markdown content is stored in **`docs/`**, and it is configured to build into **`.docs/`** (which is gitignored). A view in the `iris` app passes built docs content to the proper urls (http://localhost:8000/docs).

Use `mkdocs serve -a localhost:8001` to view the docs in a browser during development (separate from the AFRH-IRIS frontend).

Use `mkdocs build` to regenerate the static docs pages that will be served to the AFRH-IRIS frontend.

The docs can be hidden behind specific Django user permissions, but this is not implemented at the moment (doesn't make a lot of sense as the raw markdown is available on GitHub anyway).
