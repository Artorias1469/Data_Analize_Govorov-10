#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from threading import Thread
from queue import Queue

E = 1e-7  # Точность

def series1(x, eps, queue):
    s = 0
    n = 0
    while True:
        term = (-1)**n * x**(2*n) / math.factorial(2*n)
        if abs(term) < eps:
            break
        s += term
        n += 1
    queue.put(s)

def series2(x, eps, queue):
    s = 0
    n = 1
    while True:
        term = (-1)**(n-1) * x / n
        if abs(term) < eps:
            break
        s += term
        n += 1
    queue.put(s)

def main():
    x1 = 0.3
    control1 = math.cos(x1)

    x2 = 0.4
    control2 = math.log(x2 + 1)

    queue1 = Queue()
    queue2 = Queue()

    thread1 = Thread(target=series1, args=(x1, E, queue1))
    thread2 = Thread(target=series2, args=(x2, E, queue2))

    thread1.start()
    thread2.start()

    sum1 = queue1.get()
    sum2 = queue2.get()

    thread1.join()
    thread2.join()

    print(f"x1 = {x1}")
    print(f"Sum of series 1: {sum1:.7f}")
    print(f"Control value 1: {control1:.7f}")
    print(f"Match 1: {round(sum1, 7) == round(control1, 7)}")

    print(f"x2 = {x2}")
    print(f"Sum of series 2: {sum2:.7f}")
    print(f"Control value 2: {control2:.7f}")
    print(f"Match 2: {round(sum2, 7) == round(control2, 7)}")

if __name__ == "__main__":
    main()
