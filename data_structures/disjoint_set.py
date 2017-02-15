class UnionFind(object):
	def __init__(self,key,value=None):
		self.key        = key
		self.value 		= value 
		self.parent 	= None
		self.size       = 1
	
	def find(self):
		prev        = None
		current     = self
		while current:
			prev    = current
			current = current.parent
		return prev

	def union(self,element):
		setName      = self.find()
		otherSetName = element.find()
		if otherSetName.size < self.size:
			otherSetName.parent = self
			self.size += otherSetName.size
		else:
			self.parent = otherSetName
			otherSetName.size += self.size

	def compress(self):
		name    = self.find()
		current = self
		while current.parent:
			parent         = current.parent
			current.parent = name
			current        = parent

if __name__=='__main__':
	import numpy as np