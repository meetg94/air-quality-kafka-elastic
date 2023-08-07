from kafka import KafkaProducer
import json
import time
import random

#Creating a producer instance
producer = KafkaProducer(
	bootstrap_servers='localhost:9092',
	value_serializer=lambda v:json.dumps(v).encode('utf-8')
)

#List of sensors
sensors = ['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5']

while True:
	#Generating random readings
	reading = {
		'sensor_id': random.choice(sensors),
		'location': {
		'lat': round(random.uniform(-90, 90), 6),
                'lon': round(random.uniform(-180, 180), 6),
		},
		'timestamp': time.time(),
		'readings': {
			'PM2.5': random.uniform(0, 500),
			'PM10': random.uniform(0, 500),
			'CO2': random.uniform(0, 5000),
		},
	}

	producer.send('air_quality', reading)

	time.sleep(1)
