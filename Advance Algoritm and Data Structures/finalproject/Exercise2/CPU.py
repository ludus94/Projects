
from threading import Thread
import time


class CPU(Thread):
    __slots__ = 'scheduler'

    def __init__(self, scheduler):
        Thread.__init__(self)
        self.scheduler = scheduler

    def run(self):
        while True:
            try:
                job = self.scheduler.get_job()
                name = job[1][0]
                length = job[1][1]
                print("\nadd job ", name, " with length ", length, " and priority ", job[0])
                count = 0
                time.sleep(1)
                while count < length:
                    count += 1
                    print("\nin process:", name)
                    time.sleep(1)
            except:
                print("no new job this slice\n")
                time.sleep(1)
