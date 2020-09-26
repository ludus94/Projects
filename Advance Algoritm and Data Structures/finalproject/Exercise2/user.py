from random import randint
from threading import Thread
import time

class User(Thread):
    def __init__(self, scheduler):
         Thread.__init__(self)
         self.scheduler=scheduler

    def run(self):
        while True:
            probability = randint(0, 5)
            if probability == 3:
                name = "Task" + str(randint(0, 50))
                self.scheduler.add_job(randint(-20, 19), name, randint(1, 100))
            time.sleep(1)
