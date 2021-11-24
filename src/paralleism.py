import time
import multiprocessing
def f(i):
    for p in range(3):
        time.sleep(i+1)
        print('Process #',i,"\n")
        time.sleep(i)
    return
 
# start threads by passing function to Thread constructor


if __name__ == '__main__':  
    processes = []

    for i in range(3):
        t = multiprocessing.Process(target=f, args=(i,))
        processes.append(t)
        t.start()

    for one_process in processes:
        one_process.join()

    print("Done!")