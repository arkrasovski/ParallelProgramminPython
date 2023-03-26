'''
This is a sample Python script.
Press Shift+F10 to execute it or replace it with your code.
 Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
import math
from queue import Queue
from threading import Thread
import time
import pandas as pd


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n   # тут было float(n)
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i*h
        s += f(x)
    return h * s


def factorial(n):
    product = 1
    for i in range(1, n):
        product = product * (i+1)
    return product


def series_formula(x, n):
    return (-1)**n * x**(4*n + 3) / (factorial(2*n+1) * (4*n+3))


def series_method(b, n):
    sum = 0
    for i in range(n+1):
        sum += series_formula(b, i)
    #print('%.3e' % sum)
    return sum


def integrate_s(b, tol):
    n = 0
    old_result = series_method(b, n)
    while True:
        n += 1
        new_result = series_method(b, n)
        if abs(new_result - old_result) < tol:
            return new_result
        old_result = new_result


def integrate(f, a, b, tol):
    n = 1
    old_result = trapezoidal_rule(f, a, b, n)
    while True:
        n *= 2
        new_result = trapezoidal_rule(f, a, b, n)
        if abs(new_result - old_result) < tol:
            return new_result
        old_result = new_result


def f(x):
    return math.sin(x**2)


values_A = [1, 2, 3, 4, 5, 6, 7, 10]


def find_values_tr (f, a, tol, q):
    start_time = time.time()
    for i in values_A:
        q.put(integrate(f, a, i, tol))
    end_time = time.time()

    global t_tr_time
    t_tr_time = end_time - start_time
    print("ex_time trapezia =", t_tr_time)



def find_values_sr (tol, q):
    start_time = time.time()
    for i in values_A:
        q.put(integrate_s(i, tol))
    end_time = time.time()

    global t_sr_time
    t_sr_time = end_time - start_time
    print("ex_time series =", t_sr_time)

a = 0
tol = 0.000001

q_tr = Queue()
q_sr = Queue()


t_tr = Thread(target=find_values_tr, args=(f, a, tol, q_tr))
t_sr = Thread(target=find_values_sr, args=(tol, q_sr))

t_tr_time = 0
t_sr_time = 0

start_time = time.time()

t_tr.start()
t_sr.start()

t_tr.join()
t_sr.join()

end_time = time.time()
print("ex_time ", end_time - start_time)

lst_tr = list(q_tr.queue)
lst_sr = list(q_sr.queue)

pd.set_option('display.max_columns', None)
df = pd.DataFrame([lst_tr, lst_sr], columns=["A1", "A2", "A3", "A4","A5", "A6", "A7", "A10"])
df.index = ["По формуле трапеций: ", "Разложение в ряд: "]
print(df)