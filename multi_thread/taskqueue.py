import queue
import threading
class TaskQueue:
    def __init__(self, max):
        self.queue = queue.Queue(maxsize=max)
        self.lock = threading.Lock()
    
    def is_full(self):
        return self.queue.full()

    def push(self, task):
        self.queue.put(task)

    def shift(self):
        self.lock.acquire() 
        task = self.queue.get()
        self.lock.release()
        return task
        