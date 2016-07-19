import numpy as np 
import Queue 
import copy






# TODO:
# change queue object to my own queue
# clean up 'assign' function




'''
Simulates evolutionary dynamics of population with pairwise matching in a symmetric 2x2 game
'''




# population of agents implemented as a binary_search tree
# agent is node in tree

class agent(object):


	def __init__(self,index,strategy):

		if not (strategy == 'C' or strategy == 'D'):
			raise ValueError('strategy takes value in {C,D}')

		
		self.index = index
		self.strategy = strategy
		
		self.left = None
		self.right = None
		self.parent = None




	def children(self):
		
		ch = []

		if self.left:
			ch.append(self.left)
		if self.right:
			ch.append(self.right)

		return ch




	# search the subtree generated by self for s_index
	def search(self,s_index):

		if self.index == s_index:
			return self
		
		elif self.index <= s_index:
			
			if self.right:
				return self.right.search(s_index)
			else:
				return None


	

	# insert new agent into subtree spanned by agent
	def insert(self,n_agent):
		
		if not isinstance(n_agent,agent):
			raise TypeError('insert expects type(agent)')


		current = self
		while current:
			prev = current

			if current.index == n_agent.index:
				raise ValueError('index already in tree')

			if current.index < n_agent.index:
				current = current.right
			else:
				current = current.left

		if prev.index <= n_agent.index:
			prev.right = n_agent
		else:
			prev.left = n_agent

		n_agent.parent = prev







	def delete(self):
		if not self.children():
			
			if self is self.parent.left:
				self.parent.left = None
			else:	
				self.parent.right = None
		
		elif self.left and not self.right:
			
			self.parent.left = self.left
			self.left.parent = self.parent

		elif self.right and not self.left:
			
			self.parent.right = self.right
			self.right.parent = self.parent

		else:
			current = self.right
			
			while current:
			
				prev = current
				current = current.left
			
			if self is parent.left:
			
				self.parent.left = prev
				prev.parent = self.parent
			
			else:
				self.parent.right = prev
				prev.parent = self.parent





	def inOrder(self):
		
		res = []
		stack = []

		stack.append(self)
		current = self

		while stack:

			while current.left:

				stack.append(current)
				current = current.left

			while stack:
				
				current = stack.pop()
				res.append((current.index,current.strategy))
				
				if current.right:
					current = current.right
					stack.append(current)
					break

		return res


class agent_tree(object):



	def __init__(self):
		self.root = None
		self.size = 0




	def insert(self,agent):
		
		self.size += 1

		if not self.root:
			self.root = agent
		else:
			self.root.insert(agent)


	def search(self,index):
		if not self.root:
			return None
		else:
			return self.root.search(index)

	def delete(self,index):

		self.size -= 1 

		if self.root:
			d = self.root.search(index)
			if d:
				d.delete()
		
		if self.size == 0:
			self.root = None




	def select(self,alpha=.01):

		if not self.root:
			raise ValueError('tree empty')


		# compute number of agents to be selected
		N = np.floor(alpha*self.size)

		# if N is odd, add 1
		if N%2 != 0:
			N+=1 

		# assert N is even
		assert N%2 == 0


		# traverse agent tree by depth first search
		# each agent is added with probability alpha
		# until N agents are added

		selected = []

		Q = Queue.Queue()
		Q.put(self.root)

		while len(selected) < N:

			current = Q.get()

			if np.random.rand() <= alpha:
				selected.append(current)

			for child in current.children():
				Q.put(child)

		# assert that N agents have been selected
		assert len(selected) == N

		return selected



	def permutation(self,indices,start,finish):

		assert len(indices)%2 == 0

		if finish - start <= 1:

			n = np.random.randint(start+1,finish+1)
			indices[finish],indices[n] = indices[n],indices[finish]
			
			return indices

		# pick a random index
		n = np.random.randint(start+1,finish+1)

		# swap indices[start] and indices[finish]
		indices[finish],indices[n] = indices[n],indices[finish]

		return self.permutation(indices,start+1,finish-1)



	def assign(self,originalList):

		# two copies of list are needed to randomize list
		randomizedList = copy.copy(originalList)
		
		N = len(randomizedList)
		assert N%2 == 0

		randomizedList = self.permutation(randomizedList,0,N-1)


		for index in xrange(len(randomizedList)/2):
			
			old = randomizedList[index]
			new = randomizedList[N-index-1] 

			old_index = originalList.index(old)
			new_index = originalList.index(new)

			originalList[new_index] = old
			originalList[old_index] = new

		return originalList



	def match(self,alpha):

		# select agents
		selected = self.select(alpha)
		N = len(selected)

		# create list object to be randomized
		indices = [agent.index for agent in selected]

		# randomize indices
		permuted_indices = self.assign(indices)

		# pairs are just adjacent indices
		pairs = [(permuted_indices[i],search(permuted_indices[i+1]) for i in xrange(0,N,2)]

		for pair in pairs:
			# find agent 1 

		
		



	def inOrder(self):

		if self.root:
			return self.root.inOrder()
		else:
			return []



	def is_sorted(self):

		data = self.inOrder()

		for i in xrange(self.size-1):
			if data[i] > data[i+1]:
				return False
		return True





# game object
class symmetric_2by2_Game(object):
	
	def __init__(self,a,b,c,d):
		self.normal_form = [[a,b],[c,d]]


	def payoffs(s1,s2):
		if not (s1 in {0,1} and s2 in {0,1}):
			raise ValueError('strategy must be in {0,1}')
		return self.normal_form[s1][s2], self.normal_form[s2][s1]






# simulates evolution of population under
# symmetric 2 by 2 game with random pairwise matching
def simulate(G,simTime=100,initial_size=5000,c_fraction=.05,matching_frequency=.04,death_rate = .001,check_in=10):

	# initialize population
	population = agent_tree()

	c_counter = 0
	d_counter = 0

	while population.size < initial_size:
		
		if np.random.rand() <= c_fraction:
			new_agent = agent(population.size,'C')
			c_counter += 1
		else:
			new_agent = agent(population.size,'D')
			d_counter += 1
		
		population.insert(new_agent)

	assert population.is_sorted()

	# simulate population dynamics

	# returns fraction cooperating or defecting at any given time
	stats = [ [0,0] for i in xrange(simTime) ]


	time = 0
	while time < simTime:

		matches = population.match(matching_frequency)

		for pair in matches:
			
			# compute payoffs
			payoffs = G.payoffs(pair[0].strategy,pair[1].strategy)
			
			# insert offspring into population
			for x in {0,1}:
				for i in xrange(payoffs[x]):

					population.insert(agent(population.size+1, pair[x].strategy))
					
					if pair[x].strategy == 'C':
						c_counter += 1
					else:
						d_counter += 1

		frac_c = float(c_counter)/float(c_counter + d_counter)
		frac_d = 1 - frac_c
		
		stats[time] = [frac_c,frac_d]

		time += 1

		if time%check_in==0:
			print "simulation {}% completed".format(float(time)/float(simTime))

	return population,stats




if __name__=='__main__':

	G = symmetric_2by2_Game(10,5,20,8)

	P,_ = simulate(G)

	print _
	
