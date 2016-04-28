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
		self.depth = 1


class binary_search_tree(binary_tree):

	def insert(self,v):
		new_node = binary_node(v)
		current = self.root

		while len(current.children()) > 0:

			if v >= current.value:
				if current.right == None:
					current.insert_right(new_node)
				else:
					current = current.right
			else:
				if current.left == None:
					current.insert_left(new_node)
				else:
					current = current.left

	def return_as_array(self):

		current = self.root
		st = stack.stack()
		st.push(current)

		keep_going = True
		while keep_going:
			if current.left:
				current = current.left
				st.push(current)
			elif current.right:
				current = current.right
				st.push(current)
			else:
				keep_going = False

		arr = []
		while not st.is_empty():
			w = st.pop()
			arr.append(w.value)



if __name__=='__main__':

	def construct(max_iter):
		
		root = binary_node(np.random.rand())
		tree = binary_tree(root)

		s = stack.stack()
		s.push(root)
		iter=0
		
		while not s.is_empty() and iter < max_iter:
			v=s.pop()
			
			l=binary_node(np.random.rand())
			r=binary_node(np.random.rand())

			v.insert_left(l)
			v.insert_right(r)

			for child in v.children():
				if child != None:
					s.push(child)

			iter += 1

		return tree

	v = binary_node(4)
	t = binary_search_tree(v)
	print binary_search_tree