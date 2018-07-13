# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:43:20 2018

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

a = data['__4_5_']-data['__5_8_']
b = data['__3_6_']-data['__4_5_']


sigma1 = data['e__4_5_']-data['e__5_8_']
sigma2 = data['e__3_6_']-data['e__4_5_']
shock_index = []
PAHcon_index = []
for i in range(0,len(data)):
    if b[i]>((1.2/0.55)*(a[i]-0.3)+0.8):
        if a[i]<=0.95:
            if b[i]>1.05:
                shock_index.append(i)
    elif (b[i] - sigma2[i] <= (a[i] + sigma1[i] - 0.7)*1.4 + 0.15):
        if b[i] - sigma2[i] <= 1.65:
            PAHcon_index.append(i)

shock = data[shock_index]
PAHcon = data[PAHcon_index]
data.remove_rows(shock_index,PAHcon_index)

shock_x = shock['__4_5_']-shock['__5_8_']
shock_y = shock['__3_6_']-shock['__4_5_']
PAHcon_x = PAHcon['__4_5_']-PAHcon['__5_8_']
PAHcon_y = PAHcon['__3_6_']-PAHcon['__4_5_']
#############################################
band4_5 = data['__4_5_']
band5_8 = data['__5_8_']
band3_6 = data['__3_6_']
band8_0 = data['__8_0_']
band24 = data['__24_']

a = data['__4_5_']-data['__5_8_']
b = data['__3_6_']-data['__4_5_']


sigma1 = data['e__4_5_']-data['e__5_8_']
sigma2 = data['e__3_6_']-data['e__4_5_']

YSO_index = []

a = band4_5-band5_8
b = band3_6-band4_5

for i in range(0,len(data)):
    if a[i] > 0.7:
        if b[i] > 0.7:
            YSO_index.append(i)

print(YSO_index)
    
plt.figure(figsize=(10,10))

plt.scatter(a[YSO_index],b[YSO_index], color = 'b')

plt.scatter(shock_x,shock_y, color = 'black', marker = '.')
plt.scatter(PAHcon_x,PAHcon_y,color = 'black', marker = '.')

plt.scatter(a,b)

plt.plot([-4.5, 0.415], [1.05, 1.05], 'k-', color = 'r') 
plt.plot([0.85,0.85],[4,2] , color = 'r') #[5.8] − [8.0] > 1
plt.plot([0.415,0.85],[1.05,2], color = 'r')

plt.plot([1.77,6],[1.65,1.65], color = 'r')
plt.plot([-0.3,1.77],[-1.25,1.65], color = 'r')

plt.xlabel('[4.5]-[5.8]')
plt.ylabel('[3.6]-[4.5]')
plt.xlim(-5, 8)
plt.title('YSO')