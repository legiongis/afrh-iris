# Project Setup

At the project level, we do not have/need some of the components that Arches can be configured to provide.

- User signup is not enabled
- Email delivery is not configured
- No background processing components (celery, rabbitmq, supervisor) have been setup

## Custom Templates

We have customized a few of the project templates for branding and design purposes. These are templates overrides (HTML files in `arfh_prj/templates` that match the name of default Arches templates), and include some custom CSS and JavaScript plugins in `afrh_prj/media`.