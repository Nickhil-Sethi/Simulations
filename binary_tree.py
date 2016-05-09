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
	def __init__(self,value):
		self.name = None
		self.value = value
		self.left = None
		self.right = None

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

	def insert_right(self,node):
		if not isinstance(node,binary_node):
			if self.right == None:
				raise TypeError('insert_right takes input type binary_node')
			else:
				raise TypeError('insert_right takes input type binary_node; node has right child anyway')
		if self.right != None:
			raise ValueError('node already has right child node')
		
		self.right = node




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

	# returns tree as an array
	# elements sorted in order of increasing value

	def return_as_array(self):
		if self.is_empty():
			return []

		arr = []
		st = stack.stack()

		node = self.root

		while node or not st.is_empty():
			if node:
				st.push(node)
				node = node.left
			else:
				node = st.pop()
				arr.append(node.value)
				node = node.right

		return arr
	
	def breadth_first_print(self):
		q = queue.queue()
		q.enqueue(self.root)

		while not q.is_empty():
			v = q.dequeue()
			print v.value
			for w in v.children():
				q.enqueue(w)

	def depth_first_print(self):
		
		s = stack.stack()
		node = self.root

		while node or not s.is_empty():
			if node:
				s.push(node)
				node = node.left
			else:
				node = s.pop()
				print node.value
				node = node.right

# prototype of binary search tree 
# nodes must be real valued

class binary_search_tree(binary_tree):

	def insert(self,v):
		if self.is_empty():
			self.root = binary_node(v)
			self.size += 1
			return
		
		new_node = binary_node(v)
		current = self.root

		keep_going = True
		while keep_going:

			# necessary? 
			if len(current.children()) == 0:
				keep_going = False

			if v >= current.value:
				if current.right == None:
					current.insert_right(new_node)
					keep_going = False
				else:
					current = current.right
			else:
				if current.left == None:
					current.insert_left(new_node)
					keep_going = False
				else:
					current = current.left
		
		self.size += 1

	# returns node-object if node.value == value
	# else returns None
	def binary_search(self, value, current=None):

		if self.is_empty():
			return None

		if current == None:
			current = self.root
		
		if current.value == value:
			return current
		else:
			if value < current.value:
				if current.left:
					return self.binary_search(value,current.left)
				else:
					return None
			else:
				if current.right:
					return self.binary_search(value,current.right)
				else:
					return None


if __name__=='__main__':
	b = binary_search_tree()
	for i in xrange(12):
		b.insert(np.random.randint(20))

	print b.return_as_array(),"\n"
	b.depth_first_print()

	print 
	b.breadth_first_print()
	