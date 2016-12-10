from __future__ import division

import pandas as pd
import numpy as np

from tree.binary_tree import AVLTree


MAX_SIZE  	= 400
SIM_TIME  	= 1000
rProb		= .9
dProb		= .001

population 	= AVLTree()
population.insert(0)
time 		= 0
while population.size() < MAX_SIZE and time < SIM_TIME:
	time += 1
	# print [(i.key,i.balance_factor) for i in population]

	repStack = []
	delStack = []
	for agent in population:
		if np.random.rand() < rProb:
			repStack.append(agent)
		if np.random.rand() < dProb:
			delStack.append(agent)

	for i,agent in enumerate(repStack):
		population.insert(time+i)
	for j,agent in enumerate(delStack):
		population.delete(agent.key)

print "final size: ", population.size()
print population.inOrder()
