import datetime
import pika
import os
from dotenv import load_dotenv
load_dotenv()

class Producer():
    def __init__(self, channel, start_date, end_date):
        self.channel = channel
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        current = self.start_date
        end = self.end_date
        while(end > current):
            dateformat = current.strftime("%Y%m%d")
            url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + \
                dateformat + '&type=ALL'

            self.channel.basic_publish(exchange='',
                                  routing_key='crawl_stock',
                                  body=url)                 
            current = current + datetime.timedelta(days=1)


# setting rabbitmq connection
credentials = pika.PlainCredentials(
    os.getenv('USERNAME'), os.getenv('PASSWORD'))
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', credentials=credentials))

channel = connection.channel()
channel.queue_declare(queue='crawl_stock')

start = datetime.date(2013, 1, 2)
end = datetime.date(2013, 2, 10)

# start producer
p = Producer(channel, start_date=start, end_date=end)
p.run()
