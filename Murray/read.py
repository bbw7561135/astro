#!/usr/bin/env python

import csv
import sys
import numpy as np
import scipy as sp


with open('data.tsv','rb') as f:
	reader = csv.reader(f)
	data = list(reader)
###########################clean#################
print('---------------------------')
for i in range(1,114):
	data.remove(data[1])
for i in range(1,7):
	data.remove(data[len(data)-1])
############################################
new = []
for i in data:
	for j in i:
		new.append(j.split(';'))
del new[0]
for i in range(0,20):
	print new[i]




