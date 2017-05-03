#!/usr/bin/env python

#import numpy as np
import os
from numpy import *
import numpy.numarray as na
import matplotlib.pyplot as plt
from scipy.stats import stderr as err

def listdirs(folder):
    return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
m = listdirs("./results_WFD")

# scan all maps
#maps = filter(os.path.isdir,os.listdir("./results_wfd"))
#maps = filter(os.path.isdir, os.listdir('.'))
maps = m
#print maps
xlabels = []
means = zeros(0)
stds = zeros(0)

if '.svn' in maps:
	maps.remove('.svn')
maps.remove('simulation.clf')
first = True

import glob
import numpy.numarray
import shutil

for currMap in maps:
	xlabels.append(currMap)
	dataFFD = genfromtxt("results_ffd_and_wolfram/" + currMap + "/executions/partial_ffd_executions.txt")
	dataWFD = genfromtxt("results_ffd_and_wolfram/" + currMap + "/executions/exploration_execution_rafael.txt")
	dataWolfram = genfromtxt("results_ffd_and_wolfram/" + currMap + "/executions/exploration_execution_wolfram.txt")
	dataWfdINC = genfromtxt("results_wfd_INC/" + currMap + "/executions/exploration_execution_wfdINC.txt")


	wfd_ip_files = glob.glob("results_wfd_IP/" + currMap + "/executions/exploration_execution_wfdIP*.txt")
	wfd_ip_files = sort(wfd_ip_files)

	os.system("rm results_wfd_IP/" + currMap + "/executions/exploration_execution_wfdIP_merged.txt")
	wfd_merged_file = open("results_wfd_IP/" + currMap + "/executions/exploration_execution_wfdIP_merged.txt","a")
	for wfd_ip_file in wfd_ip_files:
		print "I'm in" , wfd_ip_file
		currWFDfile = open(wfd_ip_file)
		shutil.copyfileobj(currWFDfile, wfd_merged_file)
		currWFDfile.close()
	wfd_merged_file.close()

	dataWfdIP = genfromtxt("results_wfd_IP/" + currMap + "/executions/exploration_execution_wfdIP_merged.txt")

	dataFFD = dataFFD[:,1]
	
	# read data of WFD_Inc
	'''t	
	dataWfdInc = array([])
	for i in range(0,30):
		import os
		if not os.path.isfile(currMap + "/executions/exploration_execution_wfdInc_%d.txt" % i):
			continue
		tempData = genfromtxt(currMap + "/executions/exploration_execution_wfdInc_%d.txt" % i)
		dataWfdInc = append(dataWfdInc, tempData)
	'''	
	# check IF NEEDED CLIPPING!!!!!1
	# WFD works on a world smaller by 8X8 so factor it to 64
	dataWFD = 64*dataWFD
	dataWfdINC = 64*dataWfdINC
	dataWfdIP = 64*dataWfdIP

	#print log(dataFFD.std()), log(dataWFD.std()), log(dataWfdOPT.std()), log(dataWolfram.mean())
	#print log(dataWfdOPT.std()), log(dataWfdOPT.mean()), dataWfdOPT.mean() - dataWfdOPT.std(), dataWfdOPT.mean() , dataWfdOPT.std()

	#currMeans = concatenate(([],[dataWfdOPT.mean()]),0)
	#currStds =  concatenate(([],[dataWfdOPT.std()]), 0) 
	currMeans = concatenate(([],[dataWfdIP.mean(), dataFFD.mean(), dataWfdINC.mean(),  dataWFD.mean(), dataWolfram.mean()]),0)
	currStds =  concatenate(([],[err(dataWfdIP),   err(dataFFD)    ,err(dataWfdINC), err(dataWFD),   err(dataWolfram)]), 0) 
	
	if first:
		means = currMeans
		stds = currStds
		first = False
	else:	
		means = vstack((means, currMeans))
		stds = vstack((stds, currStds))
	#means = concatenate((means, currMeans),0)
		
	
	#stds = concatenate((stds, currStds),0)
	


ind = arange(len(means))
width = 0.15

fig = plt.figure()
ax = fig.add_subplot(111)

#plt.yscale('log')
offset = 0
rectList = []
colors = ['#00bfff','#ffefd5','#ffff00','#ff0000','#9400d3']
#colors = ['#fafad2', 'Cyan', 'Green', 'Red', 'Yellow']
for i in range(len(means[0])):
	rectList.append(ax.bar(ind+width*i , means[:,i], width, yerr=stds[:,i], log=True, color=colors[i]))
	#offset += width

#for i in range(cols):
#	currBars = means[:,i]


# add some labels
ax.set_ylabel('logscale time (microseconds)')
ax.set_xticks(ind+width*2.5)
ax.set_xlabel('environments')
ax.set_xticklabels( ('(A)', '(B)', '(C)', '(D)', '(E)'), fontsize=13 )
ax.grid(b=True,which='major')


def getFirst(x):
	return x[0]

#import pylab as plot
#params = {'legend.fontsize': 10,
#          'legend.linewidth': 2}
#plot.rcParams.update(params)

ax.legend(map(getFirst, rectList), ('$WFD_{IP}$', '$FFD$', '$WFD_{INC}$', '$WFD$','$SOTA$'))
#ax.legend(map(getFirst, rectList), ('$FFD$',  '$WFD$','$SOTA$'))
plt.ylim(10**5,10 ** 10)
#plt.show()



plt.savefig('plot_Results.png')
plt.savefig('plot_Results.eps')

if 1==2:
	# plot mean graph
	xlocations = na.array(range(len(means)))+0.5
	plt.bar(xlocations, means, color='Cyan')
	plt.xlabel("particles")
	plt.ylabel("average run-time (microseconds)")
	plt.grid(b=True,which='major')

	plt.hold(True)

	# plot error bars
	plt.errorbar(range(1,len(means)+1),means,stds)

	import  matplotlib.pyplot as p
	p.xlim(0,len(means)+1)

	#plt.show()
	p.savefig("matan.png")

