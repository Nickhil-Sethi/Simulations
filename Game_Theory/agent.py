import sys
sys.path.insert(0,'/Users/Nickhil_Sethi/Code/Simulations')
import binary_tree as btree
import numpy as np

class agent(btree.binary_node):

	def __init__(self,index,strategy):

		if not strategy in {'cooperate','defect','tit_for_tat'}:
			raise ValueError('strategy must be in {cooperate,defect,tit_for_tat}')

		btree.binary_node.__init__(self,index,strategy)
		self.history = None

	def play(self):

		if self.strategy == 'cooperate': 
			return 0
		elif self.strategy == 'defect':
			return 1
		else:
			return self.history

	def insert(self,agent):
		btree.binary_node.insert(self,agent)

	def search(self,agentIndex):
		return btree.binary_node.search(self,agentIndex)

	def deleteAgent(self,agent):
		btree.binary_node.deleteNode(self,agent)

	def inOrder(self):
		return btree.binary_node.inOrder(self)

class agent_tree(btree.binary_tree):

	def __init__(self):
		btree.binary_tree.__init__(self)

	def insert(self,new_agent):

		if not isinstance(new_agent,agent):
			raise TypeError('new agent must be type agent')

		btree.binary_tree.insert(self,new_agent)

	def search(self,s_index):
		return btree.binary_tree.search(self,s_index)

	def delete(self,d_index):
		btree.binary_tree.delete(self,d_index)

	def inOrder(self):
		return btree.binary_tree.inOrder(self)


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
		pairs = [ (permuted_indices[i],search(permuted_indices[i+1])) for i in xrange(0,N,2) ] 

		for pair in pairs:
			p1 = self.search(pair[0])
			p2 = self.search(pair[1])


class community(agent_tree):
	def __init__(self):
		return


if __name__=='__main__':

	T = agent_tree()

	while T.size <= 100:
		T.insert(agent( (-1)**T.size*T.size,'cooperate' ) )
	
	D = T.inOrder()
	print D

