# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:40:33 2018

@author: harrisab2
"""

import pandas as pd
import matplotlib.pyplot as plt

### import dataframe
dataFrame = pd.read_csv('Kumpula-June-2016-w-metadata.txt', skiprows=8)

### set axis values
x = dataFrame['YEARMODA']
y = dataFrame['TEMP']

#plt.plot(x, y)

### set color red and dashed
#plt.plot(x,y, 'ro--')

### tidy up
#plt.title('Kumpula temperature in June 2016')
#plt.ylabel('Temperature [F]')
#plt.xlabel('Date')
#plt.axis([20160615, 20160630])

### bar plot
plt.bar(x, y)