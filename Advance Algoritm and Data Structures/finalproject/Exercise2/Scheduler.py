from threading import Thread
import time
from priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

class Scheduler(Thread):
    __slots__ = '_jobs', '_adaptable_queue', '_min'
    EXPIRED = 10

    def __init__(self):
        Thread.__init__(self)
        self._jobs = []  # job[i] = (locator, waitingTime=0)
        self._adaptable_queue = AdaptableHeapPriorityQueue()
        self._min = None

    def run(self):
        while True:
            for job in self._jobs:
                if job[1] > self.EXPIRED and job[0]._key > -20:
                    self._adaptable_queue.update(job[0], job[0]._key - 1, job[0]._value)
                    job[1] = 0
                else:
                    job[1] += 1
                if self._min is None:
                    self._min = job
                elif self._min is not None and job[0]._key < self._min[0]._key:
                    self._min = job
                print(job)
            print("\n")
            time.sleep(1)

    def add_job(self, priority, name, length):
         loc = self._adaptable_queue.add(priority, (name, length))
         self._jobs.append(list((loc, 0)))

    def get_job(self):
        self._jobs.remove(self._min)
        self._min = None
        return self._adaptable_queue.remove_min()
