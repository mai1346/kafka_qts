import numpy as np
from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:19092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['numpy_test'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print(f'Received message: {np.frombuffer(msg.value())}')

c.close()