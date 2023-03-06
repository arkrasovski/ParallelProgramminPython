import threading
import time
from threading import Thread
from typing import Final


NUMBER_OF_SPECTATORS: Final = 30000
lock = threading.Lock()


def change_num_of_spectators(j):
    global NUMBER_OF_SPECTATORS
    i = 0

    while True:
        with lock:
            if NUMBER_OF_SPECTATORS > 0:
                NUMBER_OF_SPECTATORS = NUMBER_OF_SPECTATORS - 100 - i * 10
                i += 1
            else:
                break
        time.sleep(0.1)
        print(j, NUMBER_OF_SPECTATORS)



def main(num_of_threads):

    global NUMBER_OF_SPECTATORS
    threads = [
        Thread(target=change_num_of_spectators, args=(j, ))
        for j in range(0, num_of_threads)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()



time_of_execution = [None] * 10 # инициализация списка, без нее не работает

for i in range(1, 10 + 1):
    start_time = time.time()
    main(i)
    NUMBER_OF_SPECTATORS = 30000
    end_time = time.time()
    time_of_execution[i-1] = end_time - start_time

print(min(time_of_execution), "оптимальное число потоков: ",   time_of_execution.index(min(time_of_execution)) + 1)

print(time_of_execution)
