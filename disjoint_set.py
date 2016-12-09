from collections import deque

class element(object):
	def __init__(self,value):
		self.value 		= value 
		self.parent 	= None
		self.children 	= set()

	def items(self):
		items	= []
		queue 	= deque()
		queue.appendleft(self)
		while queue:
			current = queue.pop()
			if not isinstance(current,DisjointSet):
				items.append(current)
			for child in current.children:
				queue.appendleft(child)
		return items

	def make_child(self,child):
		old_parent 		= child.parent
		if old_parent:
			old_parent.children.remove(child)

		child.parent 	= self
		self.children.add(child)

	def find(self):
		current = self
		prev 	= None
		while current:
			prev 	= current
			current = current.parent
		return prev

	def path_compress(self):
		name 		= self.find()
		queue 		= deque()
		while queue:
			current = queue.pop()
			name.make_child(current)
			for child in current.children:
				queue.appendleft(child)

	def __repr__(self):
		return "element {}".format(self.value)

class DisjointSet(element):
	def __init__(self,name):
		element.__init__(self,name)
		self.name = self.value

	def insert(self,newElement):
		assert isinstance(newElement,element)
		self.make_child(newElement)

	def union(self,other):
		assert isinstance(other,DisjointSet)
		self.make_child(other)

	def __repr__(self):
		return "set {}".format(self.name)

if __name__=='__main__':

	import numpy as np
	import string
	L			= list(string.letters)

	A 			= DisjointSet('A')
	elements 	= range(10)
	for i in elements:
		A.insert(element(i))
		
	B			= DisjointSet('B')
	for i in xrange(10):
		B.insert(element(np.random.choice(L)))

	A.union(B)
	print A.items()