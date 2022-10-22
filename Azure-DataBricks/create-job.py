import requests
import json


DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 

try:

    response = requests.post('https://%s/api/2.0/jobs/create' % (DOMAIN), 
                             headers={'Authorization': 'Bearer %s' % (TOKEN)}, 
                             json={"name": "job name",
                                   "existing_cluster_id":"Cluster Id" ,
                                   "email_notifications": {"on_start": ["mail id" ],
                                                           "on_success": ["mail id"],
                                                           "on_failure": ["mail id"]},
                                   "notebook_task":{"notebook_path": 'path of the notebook'}})
    print(response.json())
except Exception as e:
    print("Error Creating job : %s" %
            (e))