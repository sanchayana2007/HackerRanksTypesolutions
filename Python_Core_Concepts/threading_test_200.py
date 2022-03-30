__author__ = 'Sanchayan'

import threading
import time
import Queue

exitFlag =0

def printtim(name,delay,counter):
    while counter:
        if exitFlag:
            exit(0)
    time.sleep(delay)
    print (threadName, time.ctime(time.time()))
    counter -= 1



class mythread(threading):
    def __init__(self,ThreadID,name,counter):
        self.ThreadID = ThreadID
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting',self.name)
        printtim(self.name,self.counter,5)
        print('Exiting',self.name)


# Create new threads
thread1 = mythread(1, "Thread-1", 1)
thread2 = mythread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread")