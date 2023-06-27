import threading
import time
from threading import current_thread

def mythread(arg1, arg2):
    print(current_thread().getName,'start')
    print('%s, %s' %(arg1, arg2))
    time.sleep(1)
    print(current_thread().getName,'stop')

for i in range(1,6,1):
    #t = mythread(i,i+1)
     t = threading.Thread(target=mythread,args=(i, i+1))
     t.start()

print(current_thread().getName,'end')