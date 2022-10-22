import requests
import json


DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 

try:
    response = requests.get('https://%s/api/2.0/jobs/runs/get-output' % (DOMAIN), 
                          headers={'Authorization': 'Bearer %s' % (TOKEN)}, 
                          json={"run_id": 'run_id',
                              })
    result=json.loads(response.content)
    print(result['notebook_output']['result'])
except Exception as e:
    print("Error Getting Job Output: %s" %
        (e))
