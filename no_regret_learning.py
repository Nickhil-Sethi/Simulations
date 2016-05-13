import numpy as np 

# memory object
# implementation of doubly linked list
# with cap on size
class memory_element(object):
	def __init__(self,value):
		self.value = value
		self.next = None
		self.prev = None

class memory(object):
	def __init__(self, max_length=100):
		self.max_length = max_length
		self.length = 0
		self.head = None
		self.tail = None

	def insert(self,input):
		element = memory_element(input)

		if self.head:
			element.next = self.head
			self.head.prev = element
			self.head = element
		else:
			self.head = element
			self.tail = element

		self.length += 1

		if self.length > self.max_length:
			
			self.tail = self.tail.prev
			self.tail.next = None

			self.length -= 1



# player and game class
class player(object):

	def __init__(self,num_strategies):

		# stores strategy --> utility for x i n
		self.num_strategies = num_strategies
		# payoff coefficients
		self.coeff = np.random.rand(self.num_strategies)
		
		# strategy space
		self.strategy = range(self.num_strategies)
		# memory object for agent
		self.memory = memory()

	def regret(self):
		emp_payoffs = [0 for i in self.strategy]

		current = self.memory.head
		while current.next:

			profile = current.value
			for strategy, payoff in enumerate(profile):
				emp_payoffs[strategy] += payoff

			current = current.next

		best_payoff = np.max(emp_payoffs)
		regrets = [best_payoff - emp_payoffs[i] for i in xrange(self.num_strategies) ]
		
		return regrets

	def choose(self):

		if self.memory.length == 0:
			return np.argmax(self.coeff)

		reg = self.regret()
		return np.argmin(reg)

class coordination_game(object):

	def __init__(self,N=2,S=2):

		self.N = N
		self.S = S
	
		player = {}
		for i in xrange(self.N):
			player[i] = player()
			player[i].strategy = range(self.S)

	def simulate(T = 1000):

		for i in xrange(T):
			s_profile = [player[i].choose() for i in xrange self.N]
			for player,strategy in enumerate(s_profile):
				s_counter[strategy] += 1
			



if __name__ == '__main__':

	G = coordination_game()
	
	for i in xrange(1000):
		p.memory.insert( [np.random.rand() for i in xrange(5)] )
