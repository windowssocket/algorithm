import threading
import time

balance = 0
lock = threading.Lock()

def test1():
    global balance
    print "test1"
    while True:
        lock.acquire()
        for i in range(1000):
            balance += i
        lock.release()
        time.sleep(2)


def test2():
    global balance
    print 'test2'
    while True:
        lock.acquire()
        for i in range(1000):
            balance -= i
        lock.release()
        time.sleep(2)

def dprint():
    global balance
    while True:
        print balance
        time.sleep(10)


threads = []
t1 = threading.Thread(target=test1, name='test1')
t2 = threading.Thread(target=test2, name='test2')
t3 = threading.Thread(target=dprint, name='test3')
threads.append(t1)
threads.append(t2)
threads.append(t3)


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


t1.run()
t2.run()
t3.run()

