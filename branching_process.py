from __future__ import division

import pandas as pd
import numpy as np

from tree.binary_tree import AVLTree


MAX_SIZE  = 100
SIM_TIME  = 1000
population = AVLTree()
print "initial size: ", population.size()


time = 0
while population.size() < MAX_SIZE and time < SIM_TIME:
	time += 1
	population.insert(np.random.randint(10000))


print "final size: ", population.size()
print population.inOrder()

