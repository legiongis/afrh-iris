# Management Commands

The `iris` app contains a few custom management commands.

`python manage.py initialize [operation]` - This command facilitates operations that are useful during initialization and testing.

- `groups` - Create the five user groups that are needed to support [permissions](/docs/permissions)
- `map-layers` - Rename the default Arches basemaps layers, and load the [historical map layers](/docs/map-layers)
- `test-users` - Create five test user accounts, one per permissions group, and assign that user to the corresponding group
    - The users are named `admin1`, `admin2`, `afrh_staff`, `afrh_volunteer`, `development`, and their passwords are the same as their name.

`python manage.py validate` - This command was created to handle the resource data migration from v3 to v5/6.

`python manage.py refresh_geom_view` - Refreshes the geometry view in the database. I don't know why this command is in here.