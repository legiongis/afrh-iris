#! /usr/bin/bash

python manage.py setup_db --force

# add permission groups before loading the package (because the resource models may expect them)
python manage.py initialize groups

python manage.py packages -o load_package -s ./pkg -y

python manage.py packages -o import_business_data -s ./pkg/business_data/local/Archaeological_Zone.json -ow overwrite -di false
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Character_Area.json -ow overwrite -di false
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Master_Plan_Zone.json -ow overwrite -di false
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Historic_Area.json -ow overwrite -di false
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Person.json -ow overwrite -di false
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Management_Activity.json -ow overwrite -di false
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Information_Resource.json -ow overwrite -di false
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Inventory_Resource-fixed.json -ow overwrite -di false

# update the default map layer names, load overlays
python manage.py initialize map-layers
