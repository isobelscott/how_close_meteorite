#!/usr/bin/env python3

import pandas as pd
import numpy as np
import requests
import json
import sys
from pandas.io.json import json_normalize

""" Close to earth data pulled from NASA API. Documentation: https://ssd-api.jpl.nasa.gov/doc/cad.html"""

def uptodate_api():
    today_date = str(pd.to_datetime('today').date())
    url = 'https://ssd-api.jpl.nasa.gov/cad.api?dist-max=10LD&sort=date&date-min='
    apiurl = url + today_date
    return apiurl

def getdata(apiurl):
    futureneos = requests.get(apiurl)
    futureneos.raise_for_status()
    d = futureneos.json()
    e = d['count']
    f = d['fields']
    g = d['data']

    names, dates, distmax, magni = [], [], [], []
    for i in d['data']:
        names.append(i[0])
        dates.append(i[3])
        distmax.append(i[5])
        magni.append(i[-1])

    names, dates, distmax, magni  = np.asarray(names), np.asarray(dates), np.asarray(distmax), np.asarray(magni)

    cols = np.column_stack((names, dates, distmax, magni))
    frame = pd.DataFrame(cols)
    frame.columns = ['Asteroid Name', 'Date and time of approach', 'Closest distance to Earth (AU)', 'Magnitude']
    return frame

if __name__ == '__main__':
    apiurl = uptodate_api()
    frame = getdata(apiurl)
    print(frame)


