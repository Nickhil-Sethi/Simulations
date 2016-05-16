import numpy as np 
import copy
import matplotlib.pyplot as plt


e = .01
A = [ [e, -1.0 , 1.0], 
      [1.0, e , -1.0],
      [-1.0, 1.0 , e] ]
print "A = {}".format(A)

print "\n"

def p(v):
	if not type(v) == np.ndarray:
		raise TypeError('vector must be array')
	if not all( [ i >= 0 for i in v ] ):
		print "error in vector; {}".format(v)
		raise ValueError('entries of vector must be non-negative')

	return v/float(sum(v))

def iterate_expectation(s,alpha):
	delta = np.dot(A,p(s))
	s = s + alpha*delta
	#reference parameter! s is not being changed outside the functi
	for i,s_i in enumerate(s):
		if s_i < 0:
			s[i] = 0
	return p(s)

arr = []
v = np.array([.5,.1,.4])
eps = 10.
c = 0
check_in = 35
print v

while eps > .005:
	v_next = iterate_expectation(v,.5)
	eps = sum(abs(v - v_next))
	arr.append(v_next)
	if c%check_in == 0:
		print v_next
	c += 1
	if c == 5000:
		break

