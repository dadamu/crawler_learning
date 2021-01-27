import consumer as c
import producer as p
import taskqueue
import datetime
import sys
import os

start = datetime.date(2013, 1, 2)
end = datetime.date(2013, 2, 10)

def main():
    queue = taskqueue.TaskQueue(100)
    producer = p.Producer(queue=queue, start_date=start, end_date=end)
    consumer_1 = c.Consumer(queue=queue)
    consumer_2 = c.Consumer(queue=queue)
    consumer_3 = c.Consumer(queue=queue)
    consumer_4 = c.Consumer(queue=queue)

    producer.start()
    consumer_1.start()
    consumer_2.start()
    consumer_3.start()
    consumer_4.start()

    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
