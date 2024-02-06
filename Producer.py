from kafka import KafkaProducer
import time
import pandas as pd

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

def read_csv_loop(file_path):
    while True:
        for data in pd.read_csv(file_path, chunksize=1):
            yield data

for data in read_csv_loop('testDataSet.csv'):
    message = data.to_json().encode()
    producer.send('test', message)
    print("Mesaj başarıyla gönderildi")
    time.sleep(1)
