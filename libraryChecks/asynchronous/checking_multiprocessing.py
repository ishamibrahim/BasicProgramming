import multiprocessing
import os
from multiprocessing import cpu_count
import time
a = [3, 4, 5, 7]


def call_for_loop():
    count = 0
    for i in range(10000):
        for j in range(10000):
            count += 1
    return count

def print_squares(a):

    print(f": {a} - {pow(a, 2)}", f"worked on my {os.getpid()}")
    call_for_loop()



def main1():
    print("starting")
    start = time.perf_counter()
    processes = []
    for i in range(13):
        p1 = multiprocessing.Process(target=print_squares, args=(2,))
        p1.start()
        processes.append(p1)

    for j in processes:
        j.join()

    print("ending")
    end = time.perf_counter()
    print("total time taken", end-start, "seconds")
    # Gives the
    print(cpu_count())
################################# passing data within processes using shared memory ###########################

def add_items_to_shared_list(shared, items):
    for i in range(len(items)):

        shared[i] = items[i]

def print_items_in_list(alist):
    for i, item in enumerate(alist):
        print(f"no. {i} --> {item}")

def main2():

    mylist = [1, 2, 3, 4]
    target_list = multiprocessing.Array('i', 5)

    p1 = multiprocessing.Process(target=add_items_to_shared_list, args=(target_list, mylist))
    p2 = multiprocessing.Process(target=print_items_in_list, args=(target_list,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()


############################# passing data using manager of the server process ##############################
def add_item_to_list(mylist, item):
    mylist.append(item)

def main3():
    with multiprocessing.Manager() as manager:
        mylist = manager.list(["apple", "banana", "coconut"])
        p1 = multiprocessing.Process(target=add_item_to_list, args=(mylist, "durian"))
        p2 = multiprocessing.Process(target=print_items_in_list, args=(mylist,))

        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print(mylist)

################################# passing data using queue ################################


def add_items_to_queue(mylist, q_obj):

    for item in mylist:
        q_obj.put(item)
        print(f"sent {item}")

def retreive_items_in_queue(q_obj):
    while not q_obj.empty():
        print(f"received {q_obj.get()}")

def main4():
    alist = ["apple", "banana", "carrot"]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=add_items_to_queue, args=(alist, q))
    p2 = multiprocessing.Process(target=retreive_items_in_queue, args=(q,))

    # this acts like a buffered chan in Golang, if p2 starts about the same time as p1 then
    # p2 will find that the queue is empty.
    p1.start()
    p1.join()
    p2.start()
    p2.join()


##########################Passing data Using pipe ################################
def send_counters(conn, number_list):
    print("Starting to send numbers")

    for i in number_list:
        call_for_loop()
        conn.send(i)
        print(f"sent : {i}")


    conn.send(-1)
    print("All numbers sent")


def calculate_squares(conn):
    print("starting to receive numbers")
    while True:
        num = conn.recv()
        if num == -1:
            break
        print(f"squares of {num} : {pow(num, 2)}")
    print("all numbers received")


def main5():
    nums = [3, 5, 7]
    # Pipes act like golang's chan without buffer, the process waits till something is sent to the pipe
    # conn1 and conn2 are like the two ends of pipe, item sent from conn1 will be received at conn2 and vice versa.
    conn1, conn2 = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=send_counters, args=(conn1, nums))
    p2 = multiprocessing.Process(target=calculate_squares, args=(conn2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

######################################## Using locking to avoid race condition on shared memory ##############################
# Lock has to be released be one process before being acuired by another. Check without using locks and see that the values are random
def deposit(balance, loc):
    for i in range(10000):
        loc.acquire()
        balance.value += 1
        loc.release()
def withdraw(balance, loc):
    for i in range(10000):
        loc.acquire()
        balance.value -= 1
        loc.release()

def perform_transactions():
    balanc = multiprocessing.Value('i', 100)
    loc = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=deposit, args = (balanc, loc))
    p2 = multiprocessing.Process(target=withdraw, args = (balanc, loc))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("balace value", balanc.value)

def main6():
    for i in range(10):
        perform_transactions()
    print("Done")

################################## Using pools to distribute workloads for processes #########################
# pooling makes sure each task is taken by individual processes from a pool of workers  at the same time.
def main7():
    single_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    p = multiprocessing.Pool()
    p.map(print_squares, single_list)

main7()


