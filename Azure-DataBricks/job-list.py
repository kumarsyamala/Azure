import requests
import json


DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 

try:
    response = requests.get('https://%s/api/2.0/jobs/list' % (DOMAIN), 
                              headers={'Authorization': 'Bearer %s' % (TOKEN)})

    print(response.json())
except Exception as e:
    print("Error getting Job List: %s" %
            (e))