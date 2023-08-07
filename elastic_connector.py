from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

def create_es_client():
    cloud_id= os.getenv('CLOUD_ID')
    api_key= os.getenv('API_KEY')

    return Elasticsearch(
        cloud_id=cloud_id,
        api_key=api_key
    )
