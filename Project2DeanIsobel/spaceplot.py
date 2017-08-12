#!/usr/bin/env python3

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import space
import csv
import cufflinks as cf
import plotly

plotly.tools.set_credentials_file(username='isobelsv', api_key='LO5AlkxXslP9WPpFTHe0')
cf.set_config_file(offline=False, world_readable=True, theme='pearl')

impact = space.get_impact()
orbit = space.get_orbit()
df = space.join_things(impact, orbit)


"""
data = [go.Scatter(x=df['Perihelion Distance (AU)'], y=df['Asteroid Diameter (km)'], mode='markers', 
       marker=dict(color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)','rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
       opacity=[1, 0.8, 0.6, 0.4]))]

py.iplot(data, filename='asteroids-in-space')

"""
#cufflinks:

df.iplot(kind='bubble', x='Perihelion Distance (AU)', y='Asteroid Diameter (km)', size='Asteroid Diameter (km)', text='Name', 
         xTitle='Perihelion Distance (AU)', yTitle='Asteroid Diameter (km)', filename='asteroids-in-space')

