import random
import time
from threading import Thread

from qeqClass import QuadraticEq as QeQ

kek = QeQ(27, 74, 7)
kek.show_eq()
# print(kek.find_d())
# [x1, x2] = kek.find_roots()
# print(x1, x2)

size = 100000
portion = 20

# range(start, stop, step)
# range(4)        # [0, 1, 2, 3] 0 through 4, excluding 4
# range(1, 4)     # [1, 2, 3] 1 through 4, excluding 4
# range(1, 10, 2) # [1, 3, 5, 7, 9] 1 through 10, counting by 2s
equations = [QeQ(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for i in range(size)]



def solve_eq(arr, start, end):

    eq = arr[int(start):int(end)]
    for i in eq:
        i.find_roots()
        #time.sleep(0.1)

# def worker(argument):
#     print("поток замирает " + str(argument))
#     time.sleep(5)
#     print(argument)
#     return
#
# for i in range(10):
#     t = Thread(target=worker, args=[i])
#     t.start()

def main(portion):
    threads = [
        Thread(target=solve_eq, args=(equations, i * size / portion, size / portion * (i + 1),))
        for i in range(0, portion)
    ]
    print(len(threads))
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

for i in range(2, portion + 1, 2):
    start_time = time.time()
    main(i)
    end_time = time.time()
    print("for ", i, " number of threads time is ", end_time-start_time)