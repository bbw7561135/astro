# -*- coding: utf-8 -*-
"""
Created on Thu May 31 04:21:51 2018

@author: rundo

with catalog:	J/ApJ/813/25/table4 
YSO candidates in W49 observed with Spitzer (Saral+, 2015)
criteria: 
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


c = band5_8-band8_0
d = band4_5-band5_8
PAH_index_2 = []
for i in range(0,332442):
    if d[i] < 1.05:
        if c[i]>1:
            if d[i]<(1.05/1.2)*(c[i]-1):
                if band4_5[i] > 11.5:
                    PAH_index_2.append(i)
        
plt.figure(figsize=(10,10))
plt.scatter(c,d)
plt.scatter(c[PAH_index_2],d[PAH_index_2], color = 'b')
plt.plot([2.2, 6], [1.05, 1.05], 'k-', color = 'r') #[4.5] − [5.8] < 1.05
plt.plot([1,1],[-3,0] , color = 'r') #[5.8] − [8.0] > 1
###[4.5] − [5.8] <(1.05/1.2) × ([5.8] − [8.0] − 1)###
def fit(t):
    return (1.05/1.2)*(t-1)
x = np.arange(1,2.2,0.1)
plt.plot(x,fit(x),color = 'r')
###
plt.xlim(-5, 6)
plt.ylim(-3, 3.5)
plt.xlabel('[5.8]-[8.0]')
plt.ylabel('[4.5]-[5.8]')
plt.title('PAH Galaxy Criteria_2 applied')
