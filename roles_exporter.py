# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This script will import Ranger roles from one cluster to another  #
#            It requires python 2.7 for now,                        #
#               Created by Ajinkya Patil                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import json
from requests import get, post
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

IMPORT_RANGER_URL = raw_input("ENTER RANGER URL:-\t")
ROLES_API = "/service/roles/roles/"
IMPORT_RANGER_ADMIN_USER = raw_input("RANGER ADMIN USER:-\t")
IMPORT_RANGER_ADMIN_PASSWORD = raw_input("RANGER ADMIN PASSWORD:-\t")
headers = {'Accept' : 'application/json'}

# Importing roles with all the configured users and groups

response = get(IMPORT_RANGER_URL + ROLES_API, headers=headers, verify=False,
               auth=(IMPORT_RANGER_ADMIN_USER, IMPORT_RANGER_ADMIN_PASSWORD))
roles_convert = json.loads(response.content)

ROLES = roles_convert['roles']
print ROLES

EXPORT_RANGER_URL = raw_input("ENTER RANGER URL:-\t")
USER_PATH_API = "/service/roles/roles/"
EXPORT_RANGER_ADMIN_USER = raw_input("RANGER ADMIN USER:-\t")
EXPORT_RANGER_ADMIN_PASSWORD = raw_input("RANGER ADMIN PASSWORD:-\t")
headers = {'Accept' : 'application/json'}

# Exporting roles with all the configured users and groups

for ROLE in ROLES :
    time.sleep(5)
    response = post(EXPORT_RANGER_URL + ROLES_API, headers=headers, json=ROLE, verify=False,
                    auth=(EXPORT_RANGER_ADMIN_USER, EXPORT_RANGER_ADMIN_PASSWORD))
    STATUS = response.status_code
    ROLENAME = ROLE['name']
    if STATUS is 200:
        print "Importing role" + ROLENAME + " with status " + str(STATUS)
    else:
        print "Import for role " + ROLENAME + " failed with status " + str(STATUS)
