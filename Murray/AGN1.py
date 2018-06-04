# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 00:28:40 2018

@author: rundo
"""

from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms


data = Table.read('asu.fit')
print(data.colnames)
print (len(data))


band4_5 = data['__4_5_']
band5_8 = data['__5_8_']
band3_6 = data['__3_6_']
band8_0 = data['__8_0_']
band24 = data['__24_']

a = band4_5-band8_0
b = band4_5
AGN_index = []

for i in range(0,332442):
    if band4_5[i] > 13.5:
        if a[i] >0.5:
            if b[i]>13.5+(a[i]-2.3)/0.4:
                AGN_index.append(i)
    elif band4_5[i] > 14.5:
        if b[i]> 14+(a-0.5):
            if b[i] > 14.5-(a-1.2)/0.3:
                AGN_index.append(i)

plt.figure(figsize=(10,10))
plt.scatter(a,b)
plt.scatter(a[AGN_index],b[AGN_index], color = 'b')

