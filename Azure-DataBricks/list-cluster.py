import requests
import json

DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 


try:
    response = requests.post(
        'https://%s/api/2.0/clusters/list' % (DOMAIN),
        headers={'Authorization': 'Bearer %s' % TOKEN},
)
    print(response.json())
except Exception as e:
    print("Error getting list of  cluster: %s" %
            (e))