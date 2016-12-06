from __future__ import division

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tree.binary_tree import AVLTree

population = AVLTree()
print population.size()

while population.size < 10:
	population.insert(np.random.randint(10))

print population.inOrder()