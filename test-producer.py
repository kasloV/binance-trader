from kafka import KafkaProducer
from json import dumps

# producer = KafkaProducer(bootstrap_servers='0.0.0.1:9092', value_serializer=lambda x: dumps(x).encode('utf-8'))
producer = KafkaProducer(bootstrap_servers='localhost:29092')

producer.send('test-1', b'abcd')
producer.flush()
print('end')
