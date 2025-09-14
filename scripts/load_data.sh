#! /usr/bin/bash

python manage.py packages -o import_business_data -s ./pkg/business_data/local/Archaeological_Zone_2025-09-06_17-43-28.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Character_Area.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Master_Plan_Zone_2025-09-14_10-56-59.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Historic_Area_2025-09-07_11-38-41.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Person.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Management_Activity_2025-09-07_09-09-45.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Information_Resource.json -ow overwrite
python manage.py packages -o import_business_data -s ./pkg/business_data/local/Inventory_Resource_2025-09-06_10-27-01.json -ow overwrite

python manage.py es reindex_database
