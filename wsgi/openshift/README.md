server_admin
============

Administrative User Interface for a Field Observation Server


Backup commands
---------------
Backup Groups data:
python manage.py dumpdata auth.Group > auth.Group.json

Backup Users data:
python manage.py dumpdata auth.User > auth.User.json

Backup observations data:
python manage.py dumpdata observations > observations/fixtures/initial_data.json