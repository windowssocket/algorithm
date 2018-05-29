import multiprocessing
import os

processes = []

lock = multiprocessing.Lock()



def worker(sign):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()


for i in range(5):
    process = multiprocessing.Process(target=worker, args=('process',))
    process.start()
    processes.append(process)

for process in processes:
    process.join()