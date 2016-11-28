import network
import numpy
import stack

class node(object):
	def __init__(self,index,value=None):
		self.index 		= index
		self.value 		= value
		self.explored	=False

class graph(object):
	def __init__(self,N,type=None):
		self.N 					= N
		self.adjacency_list 	= [set() for i in xrange(N)]
		self.nodes 				= [node(i) for i in xrange(N)]
		self.adjacency_matrix 	= None

	def bfs(self,n,search_value):
		s = stack.stack()
		s.push(n)

		while not s.is_empty():
			v = s.pop()
			if not self.nodes[v].explored:
				if self.nodes[v].value == search_value:
					return v
				self.nodes[v].explored = True
				for w in self.adjacency_list[v]:
					s.push(w)
		return None

if __name__ == '__main__':
	
	N=100

	G = graph(N)
	for i in xrange(G.N):
		G.nodes[i].value = numpy.random.randint(G.N)

	G.adjacency_list = network.construct_scale_free_graph(N,.3)
	print G.bfs(1,20)