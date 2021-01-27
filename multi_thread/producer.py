import threading
import datetime


class Producer(threading.Thread):
    def __init__(self, queue, start_date, end_date):
        super(Producer, self).__init__()
        self.queue = queue
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        current = self.start_date
        end = self.end_date
        while(end > current):
            if(self.queue.is_full()):
                continue
            dateformat = current.strftime("%Y%m%d")
            url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + \
                dateformat + '&type=ALL'
            self.queue.push(url)
            current = current + datetime.timedelta(days=1)
