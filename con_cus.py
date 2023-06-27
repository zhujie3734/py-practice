import queue
from threading import Thread,current_thread
import time
import random
from queue import Queue

queue = Queue(5)

class Producethread(Thread):
    def run(self):
        name = current_thread().getName
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            data = queue.put(num)
            print('生产者%s生产数据%s' %(name, num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者%s睡眠了%s' %(name, t))

class Consumerthread(Thread):
    def run(self):
        name = current_thread().getName
        global queue
        while True:
            num = queue.get()
            queue.task_done
            print('消费者%s消费数据%s' %(name, num))
            t = random.randint(1,3)
            time.sleep(t)
            print('消费者%s睡眠了%s' %(name, t))

p1 = Producethread(name = 'p1')
p1.start()
p2 = Producethread(name = 'p2')
p2.start()
c1 = Consumerthread(name = 'c1')
c1.start()