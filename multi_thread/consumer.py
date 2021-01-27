import threading
import datetime
import time

class Consumer(threading.Thread):
    def __init__(self, queue):
        self.queue = queue
        super(Consumer,self).__init__()

    def run(self):
        while(True): 
            url = self.queue.shift()
            print(url)
            time.sleep(2)

        

