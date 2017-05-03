#!/usr/bin/env python

#import numpy as np
import os
from numpy import *
import numpy.numarray as na
import matplotlib.pyplot as plt


def listdirs(folder):
    return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
m = listdirs("./results_wfd")

# scan all maps
maps = m
print maps
xlabels = []
means = zeros(0)
stds = zeros(0)

if '.svn' in maps:
	maps.remove('.svn')
maps.remove('simulation.clf')

Algs = listdirs(".")
print Algs


import csv

for currAlg in Algs:

	if currAlg != "results_wfd_INC":
		continue

	csvWriter = csv.writer(open('activeParticle.csv','wb'), delimiter=",")
	csvWriter.writerow(['Map', 'Changements', 'Executions', 'Percent'])
	mapLetter = ord('A')
	for currMap in maps:

		data = genfromtxt(currAlg  + "/" + currMap + "/executions/best_particle_index.txt")
		data1 = [1]
		ctrChange = 0

		# read data file
		for i in xrange(1,data.size):
			if data[i-1] == data[i]:
				data1.append(0)
			else: 
				data1.append(1)
				ctrChange += 1
		fig = plt.figure()

		# plot mean graph
		xlocations = na.array(range(len(data)))+0.5
		plt.bar(xlocations, data1)
		#plt.xlabel("particles")
		#plt.ylabel("average run-time (microseconds)")
		plt.xlabel("executions", fontsize=18)
		plt.ylabel("best particle index changed", fontsize=18)
		plt.yticks([0,1.0],['No', 'Yes'], fontsize=23)


		plt.grid(b=True,which='major')

		import  matplotlib.pyplot as p
		#p.xlim(0,len(means)+1)

		changement = 100.0*(ctrChange) / data.size
		#plt.title("Changements = %f %f/%f" % (changement, ctrChange, data.size) + "%")
		
		csvWriter.writerow(["(%s)" % chr(mapLetter), ctrChange, data.size, "%2.2f" %  changement])
		mapLetter += 1
		print mapLetter, currMap	

		import os
		mapName = os.getcwd().split('/')
		mapName = mapName[len(mapName)-1]

		#plt.show()
		tempFileName = currAlg  + "/" + currMap + "/executions/plot_best_particle_index_" + currMap.split('.')[0]
		p.savefig(tempFileName + ".png")
		p.savefig(tempFileName + ".eps")
		os.system('cp ' + tempFileName + ".png ~/workspace/Thesis/graphs/")
		os.system('cp ' + tempFileName + ".eps ~/workspace/Thesis/graphs/")
