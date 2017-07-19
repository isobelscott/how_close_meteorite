#!/usr/bin/env python

import random as rd
import numpy as np
import matplotlib.pyplot as plt

def walk(steps):
    step_list = [list((rd.randint(-1, 1), rd.randint(-1, 1)))]
    while (len(step_list)) < steps:
        step_list.append(list((rd.randint(-1, 1), rd.randint(-1, 1))))
    return step_list

if __name__ == "__main__":
    steps = 8
    walk1 = np.array(walk(steps))
    print(walk1)
    plt.plot(walk1)
    plt.title('Random Walk')
    plt.ylabel('Moves North or South')
    plt.xlabel('Moves East or West')
    plt.show()
