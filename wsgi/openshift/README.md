server_admin
============

Administrative User Interface for a Field Observation Server


Backup commands
---------------
Backup Groups data:
python manage.py dumpdata auth.Group > Group.json

Backup Users data:
python manage.py dumpdata auth.Permission > Permission.json

Backup Users data:
python manage.py dumpdata auth.User > User.json

Backup observations data:
python manage.py dumpdata observations > observations/fixtures/initial_data.json


Cloud version hosted on OpenShift
---------------
http://serveradmincloud-serveradmin.rhcloud.com/