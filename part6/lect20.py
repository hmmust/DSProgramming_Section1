import multiprocessing
import time
print(multiprocessing.cpu_count())
def printHi(n):
    sum =0
    for i in range(n):
        print(f"hi{n}")
        sum += i
        time.sleep(0.5)
    return sum
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=2)
    r1 = pool.apply_async(printHi,args=(5,)) #apply
    r2 = pool.apply_async(printHi,args=(10,))
    pool.close()
    pool.join()
    print(r1.get(),r2.get())
    print("Done!")