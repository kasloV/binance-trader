from kafka import KafkaConsumer, ConsumerRebalanceListener
from time import sleep
from json import loads

# consumer = KafkaConsumer('test-1', bootstrap_servers=['localhost:29092'], auto_offset_reset='earliest')
consumer = KafkaConsumer(
    'test-1',
    bootstrap_servers='localhost:29092',
    auto_offset_reset='earliest',
    enable_auto_commit=True)

for message in consumer:
    print(message)
# consumer.subscribe(['test'], listener=lambda x: print(x))

print('end')
