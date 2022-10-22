import requests
import json


DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 

try:
    response=requests.get('https://%s/api/2.0/jobs/runs/get' % (DOMAIN),
                                  headers={'Authorization': 'Bearer %s' % (TOKEN)}, 
                                  json={"run_id": 'run_id',
                                      })
    state=json.loads(response.content)['state']  
    job_state=state['life_cycle_state']
    print(job_state)
except Exception as e:
    print("Error Run state of job: %s" %
            (e))