This script will import roles from one ranger instance to another ranger instance on different cluster.
SSL enabled ranger works with the script.
While providing ranger URL, mind the training "/"
For example:-
IMPORT_RANGER_URL:- https://RANGER_HOST:RANGERPORT

Install necessary modules before executing the script:-
#pip install requests


Troubleshooting:-
status 200:- Roles have been migrated successfully.
status 400:- Either one if the goroup/user is mising or the role exists in ranger ui.
