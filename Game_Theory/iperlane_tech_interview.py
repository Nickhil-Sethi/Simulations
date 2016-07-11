import numpy as np

class node(object):

	def __init__(self,company,MonthsSinceSignup,MonthsSinceGameStart):
		self.company = company
		self.M1 = MonthsSinceSignup
		self.counter = MonthsSinceGameStart

class directedWeightedGraph(object):
	
	def __init__(self,N=0):

		# self.number of nodes
		self.N = N

		# node set
		self.nodes = set()
		
		# i connected to j in self.adjList[i]
		self.adjList = {}
		for n in self.nodes:
			self.adjList[n] = []

	def addNode(self,newnode):
		if not isinstance(newnode,node):
			raise TypeError('new node must be type node')
		
		self.N += 1

		self.nodes.add(newnode)
		self.adjList[newnode] = []

	def setConnection(self,i,j):
		if not (j in self.adjList[i]):
			# self.adjList[i] = (nodeObject j, weight i to j)
			self.adjList[i].append([j,1])

	# sets connection i,j to weight w
	def adjustWeight(self,i,j,w):

		for connection in self.adjList[i]:
			if connection[0] == j:
				connection[1] = w
				return
		raise ValueError('node not found')


	def findWeight(self,i,j):
		for connection in self.adjList[i]:
			if connection[0] == j:
				return connection[1]
		raise ValueError('node not found')

	def bellman_ford(self,i,j):

		if j in self.adjList[i]:
			return str(j[0]),j[1]
		else:
			routes = {}
			V = {}
			for k in self.adjList[i]:
				routes[k[0]], V[k[0]] = self.bellman_ford(k[0],j)
				

			m = np.inf
			winner = None 
			for candidate in V:
				if self.findWeight(i,candidate) + V[candidate] < m:
					winner = candidate
			
			return str(winner) + routes[winner], self.findWeight(i,winner) + V[winner]


money = {}
money['iperlane'] = [35,3]
money['mobilelane']= [45,4]



def constructGame():

	G = directedWeightedGraph()

	stack = []

	r1 = node('iperlane', 0,0)
	stack.append(r1)
	G.addNode(r1)

	r2 = node('mobilelane', 0,0)
	stack.append(r2)
	G.addNode(r2)

	while stack:

		current = stack.pop()

		if current.counter < 24:

			if current.M1 == 0:
				
				new_node = node(current.company, 6, current.counter + 6)

				G.addNode(new_node)
				G.setConnection(current, new_node)
				G.adjustWeight(current, new_node, -money[current.company][0] + money[current.company][1]*6)

				stack.append(new_node)
			else:
				# create node with same company, stay, increment counter
				new_node1 = node(current.company, current.M1 + 1, current.counter + 1)

				G.addNode(new_node1)
				G.setConnection(current, new_node1)
				G.adjustWeight(current, new_node1, money[current.company][1])

				# create node with DIFFERENT company
				if current.company == 'iperlane':

					new_node2 = node('mobilelane', current.M1 + 1, current.counter + 1)
					
					G.addNode(new_node2)
					G.setConnection(current,new_node2)
					G.adjustWeight( current, new_node2, money[current.company][1])

				else:

					new_node2 = node('iperlane', 0, current.counter + 1)

					G.addNode(new_node2)
					G.setConnection(current, new_node2)
					G.adjustWeight(current, new_node2, money[current.company][1])

				stack.append(new_node1)
				stack.append(new_node2)

	return G,r1,r2

if __name__=='__main__':

	'''

	G = directedWeightedGraph(4)

	G.addConnection(0,1)
	G.addConnection(0,2)
	G.addConnection(1,3)
	G.addConnection(2,3)

	print bellman_ford(G,0,3)
	'''

	terminals = []

	G,s1,s2 = constructGame()
	for n in G.adjList:
		if n.counter >= 24:
			terminals.append(n)


	for t in terminals:
		print G.bellman_ford(s1,t)
	for t in terminals:
		print G.bellman_ford(s2,t)
