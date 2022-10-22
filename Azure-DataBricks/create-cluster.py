import requests
import json


DOMAIN = '' #databricks domain or url
TOKEN = '' #access token from databricks 

try:
    response = requests.post(
        'https://%s/api/2.0/clusters/create' % (DOMAIN),
        headers={'Authorization': 'Bearer %s' % TOKEN},
        json={
            "cluster_name": "cluster name",
            "spark_version": "version",
            "node_type_id": "node type",
            "driver_node_type_id": 'node type',
            "autotermination_minutes": 10,
            "autoscale" : {
                "min_workers": 1,
                "max_workers": 3
            },
            "spart_env_vars": {},
            "init_scripts": [],
    }
    )
    print(response.json()['cluster_id'])

except Exception as e :
    print("Error launching cluster: %s" %
            (e))
