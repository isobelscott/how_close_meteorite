#!/usr/bin/env python

import random as rd
import numpy as np
import matplotlib.pyplot as plt
import math


def walk(steps):
    """ Take a random walk. """
    step_list = [list((rd.randint(-1, 1), rd.randint(-1, 1)))]
    while (len(step_list)) < steps:
        step_list.append(list((rd.randint(-1, 1), rd.randint(-1, 1))))
    return step_list


def distance(walk):
    """ Calculate distance journeyed with the walk. """
    total_distance = 0
    for coords in walk:
        dx = coords[0]
        dy = coords[1]

        distance = (math.sqrt(dx*dx + dy*dy)) * 2.58 # the distance in steps multiplied by the average number of feet in a step
        total_distance += distance

    return total_distance


def many_walks(walks):
    """ Take many random walks. """
    walk_list = []
    while (len(walk_list)) < walks:
         walk_list.append(walk(steps))
    return walk_list


def average_distance(walk_list, walks):
    """ Get the average distance of a walk, when the walker has taken many walks. """
    total_distance_all = 0

    for stroll in walk_list:
        for coords in stroll:
            dx = coords[0]
            dy = coords[1]
        distance = (math.sqrt(dx*dx + dy*dy)) * 2.58 # the distance in steps multiplied by the average number of feet in a step
        total_distance_all += distance

    return total_distance_all
    average_dist = (total_distance_all / walks)
    return average_dist


if __name__ == "__main__":
    steps = 8
    walk1 = np.array(walk(steps))
    print('During this walk, the walker moved as follows: ')
    print(walk1)

    distance = distance(walk1)
    distance1 = round(distance, 2)
    print('The distance journeyed on this walk is: ')
    print(str(distance1) + ' feet')

    walks = 4
    walk_list1 = many_walks(walks)
    print(walk_list1)

    avg_dist_all_walks = average_distance(walk_list1, walks)
    avg_dist_all_walks1 = round(avg_dist_all_walks, 2)
    print('The average distance journeyed on these walks is: ')
    print(str(avg_dist_all_walks1) + ' feet')


    # Visualize the random walks.
    
    print('The walks look like this: ')
    walk_list2 = np.vstack(walk_list1)
    plt.plot(walk_list2)
    plt.title('Random Walks')
    plt.ylabel('Moves North or South')
    plt.xlabel('Moves East or West')
    plt.show(block=True)


