import threading
from threading import current_thread

class thread(threading.Thread):
    def run(self):
        print(current_thread().getName,'start')
        print('run')
        print(current_thread().getName,'stop')

t = thread()
t.start()
t.join()
print(current_thread().getName,'end')
