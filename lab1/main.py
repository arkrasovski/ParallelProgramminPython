import random
import time
from threading import Thread

from qeqClass import QuadraticEq as QeQ

kek = QeQ(27, 74, 7)
kek.show_eq()
# print(kek.find_d())
# [x1, x2] = kek.find_roots()
# print(x1, x2)

# range(start, stop, step)
# range(4)        # [0, 1, 2, 3] 0 through 4, excluding 4
# range(1, 4)     # [1, 2, 3] 1 through 4, excluding 4
# range(1, 10, 2) # [1, 3, 5, 7, 9] 1 through 10, counting by 2s
equations = [QeQ(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for i in range(10 ** 6)]

size = 1000000
portion = 10


def solve_eq(arr, start, end):

    eq = arr[int(start):int(end)]
    for i in range(0, int(end)-int(start), 1):
        #print(i)

        eq[i].find_roots()

# def worker(argument):
#     print("поток замирает " + str(argument))
#     time.sleep(5)
#     print(argument)
#     return
#
# for i in range(10):
#     t = Thread(target=worker, args=[i])
#     t.start()

for i in range(portion):
    th = Thread(target=solve_eq, args=(equations, i * size / portion, size / portion * (i + 1), ))
    th.start()
