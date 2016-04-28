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

	def BFS(self,req):
		
		if not isinstance(req, types.FunctionType):
			raise TypeError('req must be type function')

		q = queue.queue()
		q.enqueue(queue.element(self.root))

		while not q.is_empty():
			v=q.dequeue()
			
			if req(v.value.value):
				return v.value			
			else:
				for child in v.value.children():
					q.enqueue( queue.element( child ) )

		return None

	def DFS(self,req):
		if not isinstance(req, types.FunctionType):
			raise TypeError('req must be type function')
		
		s = stack.stack()
		s.push( stack.element(self.root) )

		while not s.is_empty():
			v=s.pop()
			if req(v.value.value):
				return v.value
			else:
				for child in v.value.children():
					s.push(stack.element(child) )

		return None

	def DFS_recursive(self,req,begin=None):

		if not begin:
			begin = self.root

		if not isinstance(req,types.FunctionType):
			raise TypeError('req must be type function')

		if req(begin.value):
			return True
		else:
			if begin.children():
				
				v = [0,0]
				i = 0
				
				for child in begin.children(): 
					v[i] = self.DFS_recursive(req,begin=child)
					i+=1
				
				return max(v)
			
			else:
				return False

		return 

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

	def depth_first_print(tree):

		s = stack.stack()
		s.push(tree.root)

		depth=1
		
		while not s.is_empty():

			v=s.pop()
			print "node depth {}, value {}".format(depth,v.value)
			
			depth -= 1
			for child in v.children():
				s.push(child)

				depth+=1
	def breadth_first_print(tree):

		s = queue.queue()
		s.enqueue(tree.root)

		while not s.is_empty():
			
			v=s.dequeue()
			print "node value {}".format(v.value)
			
			for child in v.children():
				s.enqueue(child)

	req = lambda x : x > .5 
	tree= construct(40)

	print type(req)
	print breadth_first_print(tree)
	b = tree.BFS(req)
	print b.value