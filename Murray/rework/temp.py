from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms

data = Table.read('data_PAH&AGN_removed.fit')
PAH1 = Table.read('PAH_1.fit')
PAH2 = Table.read('PAH_2.fit')
AGN = Table.read('AGN.fit')


plt.figure(figsize=(10,10))
plt.scatter(data['__4_5_']-data['__8_0_'],data['__4_5_'])
plt.scatter(AGN['__4_5_']-AGN['__8_0_'],AGN['__4_5_'],color='b',marker='o')

plt.scatter(PAH1['__4_5_']-PAH1['__8_0_'],PAH1['__4_5_'],color='black',marker='.')
plt.scatter(PAH2['__4_5_']-PAH2['__8_0_'],PAH2['__4_5_'],color='black',marker='.')
plt.xlabel('[4.5]-[8.0]')
plt.ylabel('[4.5]')
plt.title('AGN star')