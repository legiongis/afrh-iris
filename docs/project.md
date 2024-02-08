# Project Configuration

At the project level, we do not need some of the components that Arches can be configured to provide.

- User signup is not enabled
- Email delivery is not configured
- No background processing components (celery, rabbitmq, supervisor) are implemented
- No mobile data collection application has been configured (this has been removed from future releases of Arches)

## Custom Templates

We have customized a few of the project templates for branding and design purposes. These are templates overrides (HTML files in `arfh_prj/templates` that match the name of default Arches templates), and include some custom CSS and JavaScript plugins that can be found in `afrh_prj/media`.

## Workflows

One workflow has been created to aid with the creation of management activities. In the code, this workflow consists of the following files:

    afrh_prj/plugins/management-workflow.json
    afrh_prj/templates/views/components/plugins/management-workflow.htm
    afrh_prj/media/js/views/components/plugins/management-workflow.js

!!! Important
    This workflow is still under construction.

## Functions

One function has been added to the project, named "activity_status_function". In the code, this function can be found at:

    afrh_prj/functions/activity_status_function.py

!!! Important
    This function is still under construction.

## Media Storage

In production, we have our uploaded files configured to be stored in AWS S3.
