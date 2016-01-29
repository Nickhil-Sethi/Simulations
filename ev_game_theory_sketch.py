import numpy as np 

A = np.random.randn(2,2)
print "A = {}".format(A)

print "\n"

def p(v):
	if not type(v) == np.ndarray:
		raise TypeError('vector must be array')
	if not all( [i >= 0 for i in v] ):
		print "error in vector; {}".format(v)
		raise ValueError('entries of vector must be non-negative')
	return v/float(sum(v))

def iterate_expectation(s):
	delta = np.dot(A,p(s))
	s = s + delta
	for strat in s:
		if strat < 0:
			strat = 0
	return p(s)

v = np.array([.4,.6])

for i in range(100):
	print v
	v = iterate_expectation(v)
