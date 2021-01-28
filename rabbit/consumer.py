import pika
import os
import time
from dotenv import load_dotenv
load_dotenv()

class Consumer():
    def __init__(self, channel):
        self.channel = channel
        super(Consumer,self).__init__()

    def run(self):
        self.channel.basic_consume(queue='crawl_stock',
                    auto_ack=False,
                    on_message_callback=self.consume)
        self.channel.start_consuming()
    
    def consume(self, ch, method, properties, body):
        print(body.decode('ascii'))
        time.sleep(2)
        ch.basic_ack(delivery_tag = method.delivery_tag)


# setting rabbitmq connection
credentials = pika.PlainCredentials(
    os.getenv('USERNAME'), os.getenv('PASSWORD'))
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', credentials=credentials))

channel = connection.channel()
channel.queue_declare(queue='crawl_stock')
channel.basic_qos(prefetch_count=1)

# start consumer
c = Consumer(channel)
c.run()
