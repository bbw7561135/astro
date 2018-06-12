# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 08:00:46 2018

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
'''
####################
a = band4_5-band8_0
b = band3_6-band5_8
PAH_index_1 = []
for i in range(0,332442):
    if b[i] < 1.5:
        if a[i]>1:
            if b[i]<(1.5/2)*(a[i]-1):
                if band4_5[i] > 11.5:
                    PAH_index_1.append(i)
PAH_1 = data[PAH_index_1]
data.remove_rows(PAH_index_1)  

band4_5 = data['__4_5_']
band5_8 = data['__5_8_']
band3_6 = data['__3_6_']
band8_0 = data['__8_0_']
band24 = data['__24_']
               
c = band5_8-band8_0
d = band4_5-band5_8
PAH_index_2 = []
for i in range(0,len(data)):
    if d[i] < 1.05:
        if c[i]>1:
            if d[i]<(1.05/1.2)*(c[i]-1):
                if band4_5[i] > 11.5:
                    PAH_index_2.append(i)

PAH_2 = data[PAH_index_2]
data.remove_rows(PAH_index_2)

'''
#############


a = band4_5-band5_8
b = band3_6-band4_5

shock_index = []

for i in range(0,len(data)):
    if b[i]>((1.2/0.55)*(a[i]-0.3)+0.8):
        if a[i]<=0.95:
            if b[i]>1.05:
                shock_index.append(i)
 
'''    
a_1 = PAH_1['__4_5_']-PAH_1['__5_8_']
b_1 = PAH_1['__3_6_']-PAH_1['__4_5_']
a_2 = PAH_2['__4_5_']-PAH_2['__5_8_']
b_2 = PAH_2['__3_6_']-PAH_2['__4_5_']           
'''

plt.figure(figsize=(10,10))
plt.scatter(a,b)
plt.scatter(a[shock_index],b[shock_index], color = 'b')
#plt.scatter(a_1,b_1,color = 'g')
#plt.scatter(a_2,b_2, color = 'g')
plt.xlabel('[4.5]-[5.8]')
plt.ylabel('[3.6]-[4.5]')
plt.xlim(-5, 8)
plt.title('shock')
