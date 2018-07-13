# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 02:59:16 2018

@author: rundo
"""

from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransform

data = Table.read('data_final.fit')
PAH1 = Table.read('PAH_1.fit')
PAH2 = Table.read('PAH_2.fit')
AGN = Table.read('AGN.fit')
shock = Table.read('shock.fit')
PAHcon = Table.read('PAHcon.fit')
YSO = Table.read('YSO.fit')

print(data.colnames)


c = 5.4478

HKm = data['Hmag']-data['Ksmag']
_36_45_m = data['__3_6_']-data['__4_5_']
K36m = data['Ksmag']-data['__3_6_']

HK0 = (1.33*(c*HKm - _36_45_m)-0.133)/(1.33*c-1)

_36_45_0 = _36_45_m - (HKm - HK0)*c
K36_0 = K36m-(HKm-HK0)*0.671

sigma1 = data['e__3_6_']-data['e__4_5_']
sigma2 = data['e_Ksmag']-data['e__3_6_']

YSO3_index = []
proto_index = []

for i in range(0,len(data)):
    if _36_45_0[i] - sigma1[i] > 0.101:
        if K36_0[i] - sigma2[i] > 0:
            if K36_0[i]-sigma2[i] > -2.85714*(_36_45_0[i]-sigma1[i]-0.101)+0.5:
                if data['__3_6_'][i]<15:
                    YSO3_index.append(i)
                #if data['__3_6_'][i]<15:
                    #if K36_0[i]-sigma2[i] > -2.85714*(_36_45_0[i]-sigma1[i]-0.401)+1.7:
                     #   proto_index.append(i)
                
plt.figure(figsize=(10,10))

#data[YSOII_index].write('YSOII.fit')

plt.scatter(_36_45_0,K36_0)


plt.scatter(_36_45_0[YSO3_index],K36_0[YSO3_index],color='b')
plt.scatter(_36_45_0[proto_index],K36_0[proto_index],color='r')

plt.xlabel('[3.6]-[4.5]_0')
plt.ylabel('K-[3.6]_0')

plt.title('YSO(red:protp,Class I, blue:Class II)')
data.remove_rows(YSO3_index)
data.write('data_phase2.fit')
#data[YSO3_index].write('YSO3.fit')
#data[proto_index].write('proto.fit')