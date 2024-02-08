# Management Commands

The `iris` app contains a few custom management commands.

`python manage.py initialize` - This command should be run after the database has been freshly set up. It will rename the default Arches basemaps layers, and also load the historical map fixture (see [Map Layers](/docs/map-layers).

`python manage.py validate` - This command was created to handle the resource data migration from v3 to v5/6.

`python manage.py refresh_geom_view` - Refreshes the geometry view in the database. I don't know why this command is in here.