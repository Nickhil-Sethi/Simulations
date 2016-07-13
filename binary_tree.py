'''

binary_tree module.
contains functions related to insertion, deletion, search.

nodes must be real valued

@author: Nickhil-Sethi

'''



import stack
import queue
import numpy as np
import types


# prototype of binary node object

class binary_node(object):
	def __init__(self,key,value=None):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.which = None

	def children(self):
		children = set()
		if self.left != None:
			children.add(self.left)
		if self.right != None:
			children.add(self.right)
		return children

	def insert_left(self,node):
		if not isinstance(node,binary_node):
			if self.left == None:
				raise TypeError('insert_left takes input type binary_node')
			else:
				raise TypeError('insert_left takes input type binary_node; node has left child anyway')
		if self.left != None:
			raise ValueError('node already has left child node')
		
		self.left = node
		self.left.which = 'left'

	def insert_right(self,node):
		if not isinstance(node,binary_node):
			if self.right == None:
				raise TypeError('insert_right takes input type binary_node')
			else:
				raise TypeError('insert_right takes input type binary_node; node has right child anyway')
		if self.right != None:
			raise ValueError('node already has right child node')
		
		self.right = node
		self.right.which = 'right'




# protype of binary tree object

class binary_tree(object):
	
	def __init__(self,root=None):

		if root == None:
			self.root = root
			self.depth = 0
			self.size = 0
		elif not isinstance (root, binary_node):
			raise TypeError('root must be type binary_node')
		else:
			self.root = root
			self.size = 1
			self.depth = 1


	# boolean to check if tree is null

	def is_empty(self):
		return (self.size == 0)

	# in order traversal
	def in_order(self):

		current = self.root

		ret = []
		s = stack.stack()

		while current or not s.is_empty():

			if current:
				s.push(current)
				current = current.left
			else:
				current = s.pop()
				ret.append(current.key)
				current = current.right
	
		return ret


# prototype of binary search tree 
# nodes must be real valued

class binary_search_tree(binary_tree):

	def binary_search(self, key, current=None):

		if self.is_empty():
			return None

		if current == None:
			current = self.root
		
		if current.key == key:
			return current
		else:
			if key < current.key:
				if current.left:
					return self.binary_search(key,current.left)
				else:
					return None
			else:
				if current.right:
					return self.binary_search(key,current.right)
				else:
					return None


	def insert(self,key,value=None):
		
		if self.is_empty():
			self.root = binary_node(key=key,value=value)
			self.size += 1
			return
		
		new_node = binary_node(key=key,value=value)

		prev = None
		current = self.root

		while current:
			if current.key <= key:
				prev = current
				current = current.right
			else:
				prev = current
				current = current.left

		if key >= prev.key:
			prev.right = new_node
		else:
			prev.left = new_node

		self.size += 1



	# returns node-object if node.value == value
	# else returns None


if __name__=='__main__':
	b = binary_search_tree()
	for i in xrange(12):
		b.insert(np.random.randint(10))

	print b.in_order(),"\n"
	print b.binary_search(5)

	