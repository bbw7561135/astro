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

####get rid of PAH galaxies####

###criteria 1####
a = band4_5-band8_0
b = band3_6-band5_8
PAH_index_1 = []
for i in range(0,332442):
    if b[i] < 1.5:
        if a[i]>1:
            if b[i]<(1.5/2)*(a[i]-1):
                if band4_5[i] > 11.5:
                    PAH_index_1.append(i)

plt.figure(figsize=(10,10))
plt.scatter(a,b)
plt.scatter(a[PAH_index_1],b[PAH_index_1], color = 'b')
plt.plot([3, 6], [1.5, 1.5], 'k-', color = 'r') #[3.6] − [5.8] < 1.5
plt.plot([1,1],[-3,0] , color = 'r') #[4.5] − [8.0] > 1
###[3.6] − [5.8] <(1.5/2) × ([4.5] − [8.0] − 1)###
def fit(t):
    return (1.5/2)*(t-1)
x = np.arange(1,3.1,0.1)
plt.plot(x,fit(x),color = 'r')
###
plt.xlim(-5, 6)
plt.ylim(-3, 5)
plt.xlabel('[4.5]-[8.0]')
plt.ylabel('[3.6]-[5.8]')
plt.title('PAH Galaxy Criteria_1 applied')