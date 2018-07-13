# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 06:19:27 2018

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

phase1_index = []

for i in range(0,len(data)):
    if data['e__3_6_'][i]<0.2:
        if data['e__4_5_'][i]<0.2:
            if data['e__5_8_'][i]<0.2:
                if data['e__8_0_'][i]<0.2:
                    phase1_index.append(i)

data[phase1_index].write('phase1_data.fit')