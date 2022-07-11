from kafka import KafkaConsumer, ConsumerRebalanceListener
from time import sleep
from json import loads

# consumer = KafkaConsumer('test-1', bootstrap_servers=['localhost:29092'], auto_offset_reset='earliest')
consumer = KafkaConsumer(
    'book',
    bootstrap_servers='localhost:29092',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

counter = 0
for message in consumer:
    print(counter)
    counter = counter + 1
# consumer.subscribe(['test'], listener=lambda x: print(x))

print('end')
