import requests
import json


DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 

try:
    response = requests.post('https://%s/api/2.0/jobs/run-now' % (DOMAIN), 
                            headers={'Authorization': 'Bearer %s' % (TOKEN)}, 
                            json={"job_id":"job_id"})
    print(response.json())
except Exception as e:
    print("Error Job Run: %s" %
            (e))