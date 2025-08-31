#! /usr/bin/bash

python manage.py setup_db --force

python manage.py packages -o import_business_data -s ./afrh_prj/system_settings/System_Settings.json -ow overwrite -di false

python manage.py packages -o load_package -s ./pkg -y

# add groups and permissions fixtures
python manage.py loaddata iris-groups
python manage.py loaddata iris-group-permissions

# update the default map layer names, load overlays
python manage.py initialize map-layers
