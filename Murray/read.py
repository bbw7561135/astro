#!/usr/bin/env python
#Create by Rundong Zhou
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
###############################turn into float#######
for i in new:
	for j in range(4,13):
		if i[j] != '     ':
			i[j] = float(i[j])
#################################
index = []
count = 0
candidate = []
for i in range(0,len(new)):
	if (new[i][6] != '     ') & (new[i][7] != '     '):
		if (new[i][6] > 3) & (new[i][6] < 9.5):
			if((new[i][6]-new[i][7])<1.25) & ((new[i][6]-new[i][7])>0.2):
				index.append(i+1)
				candidate.append(new[i])
				count=count+1
	else: 
		if (new[i][6] != '     ') & (new[i][9] != '     '):
			if (new[i][6] >3.5) & (new[i][6] < 9.5):
				if ((new[i][6]-new[i][9])<2.6) & ((new[i][6]-new[i][9]) > 0.4):
					index.append(i+1)
					candidate.append(new[i])
					count = count+1
print index
class1 = []
class2 = []
class3 = []
flat = []
unclassified = []
class1_index = []
class2_index = []
class3_index = []
flat_index = []
unclassified_index = []
for i in range(0,len(candidate)):
	if candidate[i][12] != '     ':
		if candidate[i][12] >= 0.3:
			class1.append(candidate[i])
			class1_index.append(index[i])
		elif (candidate[i][12] < 0.3)&(candidate[i][12]>=-0.3):
			flat.append(candidate[i])
			flat_index.append(index[i])
		elif(candidate[i][12]<-0.3)&(candidate[i][12]>-1.3):
			class2.append(candidate[i])
			class2_index.append(index[i])
		elif(candidate[i][12]<-1.6)&(candidate[i][12]>-2.7):
			class3.append(candidate[i])
			class3_index.append(index[i])
		else:
				unclassified.append(candidate[i])
				unclassified_index.append(index[i])
	else:
			unclassified.append(candidate[i])
			unclassified_index.append(index[i])
print 'Total number of stars: ', len(new)
print 'Number of candidates: ', count
#print len(index),' ',len(candidate)
print 'Class1: ',len(class1)
print 'Flat: ', len(flat)
print 'Class2: ', len(class2)
print 'Class3: ', len(class3)
print 'Unclassified: ', len(unclassified)
#for i in class1:
#	print i
