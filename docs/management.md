# Management Commands

The `iris` app contains a few custom management commands.

`python manage.py initialize [operation]` - This command facilitates operations that are useful during initialization and testing.

- `groups` - Create the five user groups that are needed to support [permissions]permissions.md)
- `map-layers` - Rename the default Arches basemaps layers, and load the [historical map layers](map-layers.md)
- `test-users` - Create test user accounts, see [permissions > Test Accounts](permissions.md#test-accounts)

`python manage.py validate` - This command was created to handle the resource data migration from v3 to v5/6.

`python manage.py refresh_geom_view` - Refreshes the geometry view in the database. I don't know why this command is in here.
