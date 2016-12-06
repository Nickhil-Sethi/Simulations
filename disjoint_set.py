from collections import deque 

class element(object):
	def __init__(self,value,parent=None):
		self.value 		= value
		self.parent 	= parent
		self.children   = []

	def find(self):
		pass

	def union(self,other):
		p 		 		= self.parent
		p.parent 		= other
		other.children.append(self)
