import multiprocessing
import time
print(multiprocessing.cpu_count())
def printHi(n):
    for i in range(n):
        print(f"hi{n}")
        time.sleep(0.5)
printHi(5)
printHi(10)