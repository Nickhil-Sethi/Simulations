import sys
sys.path.insert(0,'/Library/Python/2.7/site-packages')
import numpy as np

# parameters
cost_sick = 2.1
cost_medicine = 2.2

# number of states, number of actions
num_states = 2
num_actions = 2

# states and actions 
states=range(num_states)
actions=range(num_actions)

# transition matrices
p = np.zeros( (num_actions,num_states,num_states) )

p[0][0][0] = .9
p[0][0][1] = .1

p[0][1][0] = .1
p[0][1][1] = .9

p[1][0][0] = .1
p[1][0][1] = .9

p[1][1][0] = .6
p[1][1][1] = .4

beta = .9
V = []
A = []

print p[0]
print p[1]

# reward function
def R(a,s):
	if a==0 and s==0:
		return 10.
	if a==0 and s==1:
		return -10.
	if a==1 and s==0:
		return -5.5
	if a==1 and s==1:
		return 0.
	return

# iterate bellman equation
def iterate_bellman_equation(eps):
	
	diff = np.inf

	# initializing base case
	a0 = np.zeros( (num_actions,num_states,1) )
	for a in actions:
		for s in states:
			a0[a][s][:] = R(a,s)

	V0 = [ max(a0[:][s][:]) for s in states] 
	V.append(V0)
	A.append(0)

	n=0
	while n <= eps:
		n += 1

		V_n_minus_1 = V[n-1]
		V_n = np.zeros( (num_actions,num_states,1) )

		for a in actions:
			for s in states:
				V_n[a][s] = a0[a][s][:] + beta*sum( p[a][s][:]*(max( V_n_minus_1[:][s][:] ) ) )
		
		V_p = [ max(V_n[:][s][:]) for s in states]
		A_p = [ np.argmax(V_n[:][s][:] ) for s in states ]
		V.append(V_p)
		A.append(A_p)

	return V, A

V,A = iterate_bellman_equation(50)
for v,a in zip(V,A):
	print v[0], a