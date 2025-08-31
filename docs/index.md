# Overview

These docs will provide a comprehensive description of the AFRH-IRIS code base, and how to work with it. For more about how to work with Arches in general, see the [official documentation](https://arches.readthedocs.io). Currently, AFRH-IRIS is built from Arches v6.2.

## Organization

The AFRH-IRIS code base is organized as follows:

- **`afrh_prj/`** - This is the Arches **project**, and it holds the main application logic and settings.
    - see [Project Customizations](project.md)
    - see [Understanding Projects](https://arches.readthedocs.io/en/stable/installing/projects-and-packages/) in the Arches documentation for more context.
- **`pkg/`** - This is the Arches **package**, it holds database models, thesauri, and other configurations used during installation.
    - see [Package Content](package.md)
    - see [Understanding Packages](https://arches.readthedocs.io/en/stable/installing/projects-and-packages/#understanding-packages) in the Arches documentation for more context.
- **`iris/`** - This is a custom Django app that holds a few management commands and fixtures.
    - see [Management Commands](management.md) and [Custom Map Layers](map-layers.md)
- **`docs/`** - This is a mkdocs documentation module that holds this documentation.
    - see [Docs build](#docs-build)

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

See [permissions > Test Accounts](permissions.md#test-accounts) > Test Accounts to learn more about these accounts (and permissions in general).

The `initialize` command is also used within the clean install script. For more on that command, see [Management Commands](management.md).

!!! Warning
    Arches does not support the load of resource model-level permissions from packages. This means all permissions described in [permissions > Permissions by Resource Model](permissions.md#permissions-by-resource-model) must be implemented manually after installation.

## Docs build

This documentation is built with [mkdocs-material](https://squidfunk.github.io/mkdocs-material) and deployed/hosted through ReadTheDocs. The source markdown content is stored in **`docs/`**.

### Writing docs

Make sure you have installed mkdocs-material.

```
pip install mkdocs-material
```

Use `mkdocs serve -a localhost:8001` to preview the docs in a browser during development.

To run the buid process locally (could be helpful in some case), use `mkdocs build` and the content will be written to `.docs/` (which is gitignored).
