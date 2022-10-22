import requests
import json


DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 

try:
    response = requests.post(
        'https://%s/api/2.0/clusters/start' % (DOMAIN),
        headers={'Authorization': 'Bearer %s' % TOKEN},
        json={'cluster_id':'Cluster ID'})
    print(response.json())
except Exception as e:
    print("Error Strating cluster: %s" %
            (e))