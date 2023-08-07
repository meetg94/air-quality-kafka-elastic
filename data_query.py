from elasticsearch import Elasticsearch
from elastic_connector import create_es_client

es = create_es_client()

query = {
    'query': {
        'range': {
            'readings.PM2.5': {
                'gte': 100  # Get all readings where PM2.5 is greater than or equal to 100
            }
        }
    }
}

response = es.search(index='air_quality', body=query)

for hit in response['hits']['hits']:
    print(hit['_source'])
