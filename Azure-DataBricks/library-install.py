import requests
import json


DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 

try:
    response = requests.post(
        'https://%s/api/2.0/clusters/create' % (DOMAIN),
        headers={'Authorization': 'Bearer %s' % TOKEN},
        json={
            'cluster_id':'Cluster ID',
            'libraries' : {
                'pypi' : {'package' : 'library_name'},
                'whl' : 'wheel file location',
                'egg' : 'egg file location'}
                }
                )
    print(response.json())
except Exception as e:
        print("Error installing libraries in cluster: %s" %
            (e))