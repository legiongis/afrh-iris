#! /usr/bin/bash

python manage.py packages -o import_business_data -s ./pkg/business_data/local/Archaeological_Zone.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Character_Area.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Master_Plan_Zone.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Historic_Area.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Person.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Management_Activity.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Information_Resource.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Inventory_Resource-fixed.json -ow overwrite

python manage.py es reindex_database
