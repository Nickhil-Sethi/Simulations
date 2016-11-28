from __future__ import division

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tree.binary_tree import binaryNode

MAX_SIZE 	= 50
SIM_LENGTH 	= 1000
repr_prob 	= 1.0
del_prob	= .1

population	= binaryNode('0')
population.insert('0')

t = 0
h = 0
size = 0
sizes = []
while t < SIM_LENGTH:
	repr_stack 	= []
	del_stack   = []
	current 	= population
	in_order 	= [current]
	print "in order"
	while in_order:

		current = in_order.pop()
		if np.random.rand() < repr_prob:
			repr_stack.append(current.key)
		if np.random.rand() < del_prob:
			del_stack.append(current.key)
		if current.right:
			in_order.append(current.right)
		if current.left:
			in_order.append(current.left)
		print in_order

	print "inserting", repr_stack
	for index, agent in enumerate(repr_stack):
		population.insert(str(h))
		h += 1
		size += 1

	print "deleting", del_stack
	for agent in del_stack:
		population.delete(agent)
		size -= 1

	sizes.append( size )
	print t
	t += 1

print sizes
sizes = pd.Series(sizes)
sizes.plot()
plt.show()