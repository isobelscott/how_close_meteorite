#!/usr/bin/env python3

import csv
import pandas as pd
import numpy as np

def get_impact():
    """ get the name of the space objects and their diameter from one csv """
    with open('/Users/isobel/Downloads/asteroid-impacts/impacts.csv') as csvfile:
        impactreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        impact_name_list = []
        diameter_list = []
        for row in impactreader:
            diameter_list.append(row[7])
            impact_name = row[0].split(" ")
            if impact_name[-1][-1] == ')':
                impact_name[-1] = impact_name[-1][:-1]
            impact_name_list.append(impact_name[-1])
        a =  np.column_stack((impact_name_list, diameter_list))
        return a


def get_orbit():
    """ get the name of the space objects and their perhelion distance from another csv"""
    with open('/Users/isobel/Downloads/asteroid-impacts/orbits.csv') as csvfile:
        orbitreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        orbit_name_list = []
        orbit_peri_list = []
        for row in orbitreader:
            orbit_name = row[0].split("\xa0")
            orbit_name = orbit_name[-1][:-1]
            if orbit_name == "Object Nam": 
                orbit_name = "Name"
            orbit_name_list.append(orbit_name)
            peri_dist = row[9]
            orbit_peri_list.append(peri_dist)
        b = np.column_stack((orbit_name_list, orbit_peri_list))
        return b


def join_things(a, b):
    """ making sure only the space objects that are in both lists are present and make into a nice pandas dataframe """
    c = []
    for row in a:
        index = np.where(b[:,0] == row[0])[0]
        if np.size(index) !=0:
            c.append([row[0], row[1], b[index[0], 1]])
        else:
            c.append([row[0], row[1], 0])

    d = pd.DataFrame(c)
    d = d.ix[1:683]
    d.columns = ['Name', 'Asteroid Diameter (km)', 'Perihelion Distance (AU)']
    return d
    

def pandas_csv(df):
    """ makes the pandas df a csv """
    new_csv = df.to_csv('orbitsnimpacts.csv', header=False, index=False)
    return new_csv



if __name__ == '__main__':
    impact = get_impact()
    orbit = get_orbit()
    df = join_things(impact, orbit)
    print(df)

