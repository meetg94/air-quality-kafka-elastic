from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

from elastic_connector import create_es_client

consumer = KafkaConsumer(
    'air_quality',  
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

es = create_es_client()

for message in consumer:
    reading = message.value

    doc_id = f"{reading['sensor_id']}_{reading['timestamp']}"

    es.index(index='air_quality', id=doc_id, body=reading)
