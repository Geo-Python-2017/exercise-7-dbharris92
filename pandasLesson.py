# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:34:59 2018
Lesson 7 Pandas Plotting Lecture
@author: harrisab2
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


### declare filepath
fp = r'F:\GS\harrisab2\S18\GeoViz\Lesson7\helsinki.txt'

### import
data = pd.read_csv(fp, sep= '\s+', parse_dates=['YR--MODAHRMN'], na_values = ['*', '**', '***', '****', '*****', '******'])

### select data
selected_cols = ['YR--MODAHRMN', 'TEMP', 'SPD']
data = data[selected_cols]

### rename columns
name_conversion = {'YR--MODAHRMN': 'TIME', 'SPD': 'SPEED'}
data = data.rename(columns=name_conversion)

### convert Fahrenheit into C
data['Celsius'] = (data['TEMP'] - 32) / 1.8

### plot
#data.plot(x= 'TIME', y = 'Celsius')

### change hte index
data = data.set_index('TIME')


### select data
first_jan = data['2013-01-01': '2013-01-01']
first_jan12hr = data['2013-01-01 00:00': '2013-01-01 12:00']

### aggregate data into new dataframe with .resample() function from hourly to daily
daily= data.resample(rule='D').mean()

#daily.plot(x=daily.index, y='Celsius', kind='line', lw=0.75, c='g')

### how to save figure to disk
#plt.savefig('output path')

### create datasets for each season
winter = daily['2012-12-01': '2013-02-28']
spring = daily['2013-03-01': '2013-05-31']
summer = daily['2013-06-01': '2013-08-31']
fall = daily['2013-09-01': '2013-11-30']

### create 2x2 plots fig variable. fig is object container (graphs themselves) whereas axes is an array of all the data 
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,8))

### parse axes from the axarray created above
ax11 = axes[0] [0]
ax12 = axes[0] [1]
ax21 = axes[1] [0]
ax22 = axes[1] [1]

### create the subplots with paramter ax
winter.plot(x=winter.index, y='Celsius', ax=ax11, c='blue', lw=2.5)
spring.plot(x=spring.index, y='Celsius', ax=ax12, c='yellow', lw=2.5)
summer.plot(x=summer.index, y='Celsius', ax=ax21, c='red', lw=2.5)
fall.plot(x=fall.index, y='Celsius', ax=ax22, c='orange', lw=2.5)