import threading
import time
import hashlib

threads = []
count = 0
num = 4

class Helloworld(threading.Thread):
    def __init__(self, num):
        hash_name = hash(time.time())
        threading.Thread.__init__(self, name=hash_name)
        self._run_num = num

    def run(self):
        global count
        threadname = threading.currentThread().getName()
        mutex = threading.Lock()
        for x in xrange(0, int(self._run_num)):
            print threading.current_thread().is_alive()
            mutex.acquire()
            count = count + 1
            mutex.release()
            print threadname, x, count
            time.sleep(1)

for x in xrange(0, num):
    threads.append(Helloworld(10))

for t in threads:
    t.Daemon = True
    t.start()
    print "enumerate" + str(threading.active_count())
print
for t in threads:
    t.join()


print "helloworld"

