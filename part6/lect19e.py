import multiprocessing
import time
print(multiprocessing.cpu_count())
def printHi(n,queue):
    sum =0
    for i in range(n):
        print(f"hi{n}")
        sum += i
        time.sleep(0.5)
    queue.put(sum)
if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=printHi,args=(5,queue,))
    p2 = multiprocessing.Process(target=printHi,args=(10,queue,))
    p1.start()
    p2.start()
    p1.join()
    print(queue.get())
    p2.join()
    print(queue.get())

    print("Done!")