from Exercise2.CPU import CPU
from Exercise2.user import User
from Exercise2.Scheduler import Scheduler
from priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

if __name__ == '__main__':
    scheduler = Scheduler()
    user = User(scheduler)
    CPU = CPU(scheduler)

    scheduler.start()
    user.start()
    CPU.start()
