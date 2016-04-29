import stack
import queue
import numpy as np
import types

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


class binary_tree(object):
	
	def __init__(self,root):
		if not isinstance (root, binary_node):
			raise TypeError('root must be type binary_node')
		self.root = root
		self.size = 1
		self.depth = 1

	def return_as_array(self):

		arr = []
		st = stack.stack()

		node = self.root
		st.push(node)


		while not st.is_empty():
			if node.left:
				node = node.left
				st.push(node)
			else:
				while not st.is_empty():
					node = st.pop()
					arr.append(node.value)
					if node.right:
						node = node.right
						st.push(node)
						break

		return arr
# binary search tree on real numbers
class binary_search_tree(binary_tree):

	def insert(self,v):
		new_node = binary_node(v)
		current = self.root

		keep_going = True
		while keep_going:

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

	def binary_search(self, value, current=None):
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
	k = 20
	v = binary_node(k)
	t = binary_search_tree(v)
	for i in xrange(k,k+20):
		t.insert(i)

	print t.return_as_array()