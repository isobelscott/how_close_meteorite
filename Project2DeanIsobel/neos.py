#!/usr/bin/env python3

import pandas as pd
import numpy as np
import requests
import json

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

    dates2 = []
    times2 = []
    for date in dates:
        datetime = date.split(' ')
        date2 = datetime[0]
        dates2.append(date2)
        time2 = datetime[-1]
        times2.append(time2)
    
    
    names, dates2, times2, distmax, magni  = np.asarray(names), np.asarray(dates2), np.asarray(times2), np.asarray(distmax), np.asarray(magni)


    cols = np.column_stack((names, dates2, times2, distmax, magni))
    frame = pd.DataFrame(cols)
    frame.columns = ['Asteroid Name', 'Date of approach', 'Time of approach', 'Closest distance to Earth (AU)', 'Magnitude']
    frame['Date of approach'] = pd.to_datetime(frame['Date of approach']).dt.date
    frame['Time of approach'] = pd.to_datetime(frame['Time of approach']).dt.time
    return frame

def whats_close(frame):
    close = frame['Closest distance to Earth (AU)'].argmin()
    closedist = frame.iloc[close]['Closest distance to Earth (AU)']
    closename = frame.iloc[close]['Asteroid Name']
    closedate = frame.iloc[close]['Date of approach']
    closetime = frame.iloc[close]['Time of approach']

    return str('\n'+ 'The asteroid that will come closest to Earth is ' + closename + '.'
    '\n' + 'It will be ' + str(closedist) + ' astronomical units away' + 
    ' on ' + str(closedate) + ' at ' + str(closetime) + '\n')

def whats_soonest(frame):
    soon1 = frame['Date of approach'].min()
    soon = np.where(frame['Date of approach']==soon1)[0]
    soonname = (frame.iloc[soon]['Asteroid Name'])[0]
    soondist = (frame.iloc[soon]['Closest distance to Earth (AU)'])[0]
    soondate = (frame.iloc[soon]['Date of approach'])[0]
    soontime = (frame.iloc[soon]['Time of approach'])[0]

    return str('The soonest close approach to Earth is '
    + str(soondate) + ' at ' + str(soontime) + '.'
    + '\n' + 'The approaching NEO is called ' + soonname + ' and it will be ' + str(soondist) + ' away.'+ '\n') 
    

if __name__ == '__main__':
    apiurl = uptodate_api()
    frame = getdata(apiurl)
    closer = whats_close(frame)
    sooner = whats_soonest(frame)
    print(closer)
    print(sooner)
