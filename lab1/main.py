import random
import time
from threading import Thread
import matplotlib.pyplot as plt

from qeqClass import QuadraticEq as QeQ

kek = QeQ(27, 74, 7)
kek.show_eq()
# print(kek.find_d())
# [x1, x2] = kek.find_roots()
# print(x1, x2)

size = 1000000
portion = 10

# range(start, stop, step)
# range(4)        # [0, 1, 2, 3] 0 through 4, excluding 4
# range(1, 4)     # [1, 2, 3] 1 through 4, excluding 4
# range(1, 10, 2) # [1, 3, 5, 7, 9] 1 through 10, counting by 2s
equations = [QeQ(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for i in range(size)]



def solve_eq(arr, start, end, num):

    eq = arr[int(start):int(end)]
    print(num)
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
        Thread(target=solve_eq, args=(equations, i * size / portion, size / portion * (i + 1), i))
        for i in range(0, portion)
    ]
    print(len(threads))
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


estimate_time = []

start_time = time.time()
main(1)
end_time = time.time()
time_for_1thread = end_time-start_time  # время в секундах
print("Time for 1 thread", end_time-start_time)

for i in range(2, portion + 1, 2):
    start_time = time.time()
    main(i)
    end_time = time.time()
    estimate_time.append(end_time-start_time)
    print("for ", i, " number of threads time is ", end_time-start_time)

estimate_time.pop(2)

xlabels = [1, *range(2, portion + 1, 2)]
xlabels.remove(6)

plt.plot(xlabels, [time_for_1thread, *estimate_time], marker="o", mfc="green", mec="yellow", color="orange") #mec - цвет обводки маркера mfc - Цвет заливки маркера

plt.xlabel("Number of threads")
plt.ylabel("Time")

plt.title("Number of threads VS time")



plt.xticks(xlabels) #эта штука задает масштаб по х

plt.show()
