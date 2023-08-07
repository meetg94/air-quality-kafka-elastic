from kafka import KafkaProducer
import json
import datetime
import random
import time

#Creating a producer instance
producer = KafkaProducer(
	bootstrap_servers='localhost:9092',
	value_serializer=lambda v:json.dumps(v).encode('utf-8')
)

#List of sensors
sensors = ['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5']

def generate_reading(timestamp):
	#Generating random readings
	reading = {
		'sensor_id': random.choice(sensors),
		'location': {
				'lat': round(random.uniform(-90, 90), 6),
                'lon': round(random.uniform(-180, 180), 6),
		},
    	'timestamp': timestamp.isoformat(),
		'readings': {
			'PM2.5': random.uniform(0, 500),
			'PM10': random.uniform(0, 500),
			'CO2': random.uniform(0, 5000),
		},
	}

	producer.send('air_quality', reading)

num_readings = 1440

start_time = datetime.datetime.now() - datetime.timedelta(hours=24)

interval = datetime.timedelta(hours=24) / num_readings

for _ in range(num_readings):
	generate_reading(start_time)
	start_time += interval

while True:
	generate_reading(datetime.datetime.now())
	time.sleep(60)