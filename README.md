---

# Air Quality Monitoring System with Kafka and Elasticsearch

This project simulates an air quality monitoring system that leverages the power of Apache Kafka for real-time data streaming and Elasticsearch for data indexing and advanced querying. By using these technologies in tandem, the system is capable of efficiently processing, storing, and visualizing vast amounts of data in real-time.

## Table of Contents
1. [Overview](#overview)
2. [Technologies Used](#technologies-used)
3. [Project Architecture](#project-architecture)
4. [Setup and Installation](#setup-and-installation)
5. [Data Generation](#data-generation)
6. [Data Processing and Indexing](#data-processing-and-indexing)
7. [Visualization in Kibana](#visualization-in-kibana)
8. [Challenges and Solutions](#challenges-and-solutions)
9. [Screenshots](#screenshots)
10. [Conclusion](#conclusion)

## Overview

The objective of this system is to simulate the real-time acquisition of air quality metrics from multiple sensors distributed in various locations. These metrics include PM2.5, PM10, and CO2 concentrations.

## Technologies Used

- **Apache Kafka**: Used for real-time data streaming.
- **Elasticsearch**: A distributed search and analytics engine where the data gets indexed.
- **Kibana**: Visualization tool for Elasticsearch.

## Project Architecture

1. **Data Generator**: Simulates air quality readings from various sensors and produces this data to a Kafka topic.
2. **Data Processor**: Consumes the data from Kafka, processes it, and indexes it into Elasticsearch.
3. **Kibana Dashboard**: Visualizes the indexed data in real-time.

## Setup and Installation

1. **Kafka Setup**: 
   - Set up a local Kafka broker.
   - Create a topic named `air_quality`.

2. **Elasticsearch and Kibana Setup**:
   - Register for a free trial on Elastic Cloud.
   - Retrieve the Cloud ID and API Key for authentication.
   - Set up the `air_quality` index in Elasticsearch.

## Data Generation

The `data_generator.py` script simulates readings from five sensors. Each reading includes:

- Sensor ID
- Location (latitude and longitude)
- Timestamp
- Air quality metrics (PM2.5, PM10, and CO2 concentrations)

Initially, the script generates data for the past 24 hours. After that, it starts producing real-time readings every minute.

## Data Processing and Indexing

The `data_processor.py` script consumes data from the Kafka topic, processes it, and then indexes it into Elasticsearch. 

## Visualization in Kibana

After indexing the data, Kibana is used to create visualizations and dashboards. Some of the visualizations created include:

1. Line chart showcasing PM2.5 readings over time.
2. Pie chart representing average readings by sensor.
3. Heat map depicting CO2 concentrations over time.

## Challenges and Solutions

During the project, we faced several challenges:

1. **Data Overlap**: Since the data generator script was modified to produce data for the past 24 hours, there was a risk of overlapping data with previously indexed values. 
   - **Solution**: Deleted the existing Elasticsearch index and recreated it to start with a clean dataset.

2. **Visualization Timeframe**: Initially, Kibana visualizations were not reflecting real-time data. 
   - **Solution**: Adjusted the time range in Kibana to show recent data.

## Screenshots

![Line Chart](<img width="937" alt="Screenshot 2023-08-07 at 4 00 35 PM" src="https://github.com/meetg94/air-quality-kafka-elastic/assets/86708110/333653f2-954f-4967-b9b8-255430a25fbe">)
*Line chart of PM2.5, PM10, and CO2 readings over time.*

![Pie Chart](<img width="438" alt="Screenshot 2023-08-07 at 4 07 49 PM" src="https://github.com/meetg94/air-quality-kafka-elastic/assets/86708110/1d059710-1e23-4a2c-967c-cffdcc657b7a">)
*Pie chart showcasing average readings by sensor.*

![Heat Map]("https://github.com/meetg94/air-quality-kafka-elastic/assets/86708110/5619e5ee-805b-4a6f-b507-5ce428af1af2")
*Heat map of CO2 concentrations over the past 24 hours.*

## Conclusion

This project showcases the power and efficiency of using Kafka and Elasticsearch in tandem for real-time data processing and visualization. With this system in place, it's possible to monitor air quality metrics in real-time, enabling timely insights and actions.

---
