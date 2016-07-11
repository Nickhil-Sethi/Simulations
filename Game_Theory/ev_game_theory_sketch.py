import numpy as np 
import copy

# the structure that stores the agents
# must be amenable to random access, deletion, and insertion
# so a binary search tree is being used

class agent(object):
	def __init__(self,index,strategy):
		
		self.index = index
		self.strategy = strategy
		
		self.left = None
		self.right = None
		self.parent = None

	def search(self,s_index):
		current = self

		while current:
			if current.index == s_index:
				return current
			elif current.index <= s_index:
				current = current.right
			else:
				current = current.left
		return current


	def insert(self,n_agent):
		
		if not isinstance(n_agent,agent):
			raise TypeError('insert expects type(agent)')

		nIndex = agent.index

		current = self
		while current:
			if current.index == nIndex:
				raise ValueError('index already in tree')
			elif current.index <= nIndex:
				prev = current
				current = current.right
			else:
				prev = current
				current = current.left
		
		if prev.index <= nIndex:
			prev.right = n_agent
			n_agent.parent = prev
		
		else:
			prev.left = n_agent
			n_agent.parent = prev


	def delete(self,d_index):
		d_agent = self.search(d_index)

		if not (d_agent.left or d_agent.right):
			
			P=d_agent.parent
			
			if P.left is d_agent:
				P.left = None
			else:
				P.right = None
		
		if d_agent.left and not d_agent.right:

			P=d_agent.parent
			L = d_agent.left
			
			if P.left is d_agent:
				P.left = L
				L.parent = P

			else:
				P.right = L
				L.parent = P
		if d_agent.right and not d_agent.left:

			P=d_agent.parent
			R = d_agent.right
			
			if P.left is d_agent:
				P.left = R
				L.parent = P
			else:
				P.right = R
				L.parent = P
		else:

			current = d_agent.right
			while current:
				minRight = current 
				current = current.left
			
			d_agent.left.parent = minRight
			minRight.left = d_agent.left

def randomize_list(N):

	L=range(N)


	i = 0
	while i < N/2:

		# 
		k = np.random.randint(N-2*i)

		temp = L[N-i-1]
		L[N-i-1] = L[i+k]
		L[i+k] = temp

		i += 1

	R = []
	for i in xrange(N):
		R.append(L[N-i-1])
	return R



def random_pairwise_matching(N,k):

	if not k%2==0:
		raise ValueError('k must be even')
	
	s = np.random.choice(N,k)
	M = np.random.choice(s,k/2)
	W = list(set(s).subtract(set(M)))

	for i in xrange(k):
		q = np.random.randint()

# function interacts two strategies
def interact(payoff_matrix, v, w):

	return # payoffs v, w

def evolve(S,m,payoff_matrix):

	# error catching
	if not m%2==0:
		raise ValueError('match population must be even')

	# total size of population
	N = len(S)

	# draw m "matched" individuals

# interact drawn agents
# randomly kill with probability epsilon




if __name__=='__main__':

	'''

	# payoff matrix; 0 := cooperation , 1 := defection
	PrisonersDilemma = [ [ 1, 10], [ -10, -5 ] ]

	# population size
	N = 10000

	# starting fraction of cooperators
	c = .3

	# randomly initialize population
	f = lambda x,c : 1 if x > c else 0

	# state vector; S[i] = strategy of player i
	S = [ f( np.random.rand(), p ) for i in xrange(N) ]

	evolution(S)
	'''

	print randomize_list(10)