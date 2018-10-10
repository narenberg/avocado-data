import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import numpy;
import matplotlib.pyplot as plt;
import csv;

avgPrice = []
dates = []

with open('avocado.csv', newline='') as data:
	datereader = csv.reader(data, delimiter=',', quotechar='|')
	next(datereader)
	for row in datereader:
		dates.append([row[12], row[2]])
avgdict = {}
counts = {}
possibleyears = ['2015', '2016', '2017', '2018']
for d in possibleyears:
	avgdict[d] = 0
	counts[d] = 0
for item in dates:
	avgdict[item[0]] += float(item[1])
	counts[item[0]] += 1
print(avgdict)
for x in avgdict:
	avgdict[x]/=counts[x]
fig, axs = plt.subplots(1, 1)
axs.bar(avgdict.keys(), avgdict.values())
fig.suptitle('Average avocado price per year')
plt.savefig('graph.png')	
