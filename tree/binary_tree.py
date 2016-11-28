import pdb
class binaryNode(object):
	def __init__(self,key,value=None):
		self.key 			= key
		self.value 			= value
		self.left 			= None
		self.right 			= None

	def min_right(self):
		parent 				= None
		prev 				= self
		current 			= self.right
		while current:
			parent 			= prev
			prev 			= current
			current 		= current.left
		return prev, parent

	def insert(self,key,value=None):
		newNode 			= binaryNode(key,value)
		current 			= self
		while current:
			if current.key == key:
				return
			prev 			= current
			if current.key < key:
				current 	= current.right
			else:
				current 	= current.left

		if prev.key < key:
			prev.right 		= newNode
		else:
			prev.left  		= newNode

	def search(self,key):
		prev    = None
		current = self
		while current:
			if current.key == key:
				return current, prev
			prev = current
			if current.key < key:
				current 	= current.right
			else:
				current		= current.left
		return current, prev

	def inOrder(self):
		stack 				= [self]
		ret   				= []
		current 			= self
		while stack:
			if current.left:
				current 	= current.left
				stack.append(current)
			else:
				while stack:
					current = stack.pop()
					ret.append(current.key)
					if current.right:
						current = current.right
						stack.append(current)
						break
		return ret

	def delete(self,key):
		node,parent = self.search(key)
		if node and node != self:
			if not node.left and not node.right:
				if parent.key < node.key:
					parent.right = None
				else:
					parent.left  = None
				return
			if node.left and not node.right:
				if parent.key < node.key:
					parent.right = node.left
				else:
					parent.left  = node.left
				node.left        = None
				return
			if node.right and not node.left:
				if parent.key < node.key:
					parent.right = node.right
				else:
					parent.left  = node.right
				node.right 	     = None
				return
			if node.right and node.left:
				minRight, Rparent = node.min_right()
				if minRight == node.right:
					if parent.key < node.key:
						parent.right = minRight
					else:
						parent.left  = minRight
					minRight.left    = node.left
					node.left 		 = None
					node.right       = None
				else:
					if minRight.right:
						Rparent.left 	= minRight.right
						minRight.right  = None
					else:
						Rparent.left    = None
					if parent.key < node.key:
						parent.right = minRight
					else:
						parent.left  = minRight
					minRight.left    = node.left
					node.left        = None
					minRight.right   = node.right
					node.right       = None
				return

	def __repr__(self):
		return "key: {}, value: {}".format(self.key,self.value)

if __name__=='__main__':
	T = binaryNode(3)
	import numpy

	c = 0 
	nums = []
	while c < 100:
		c += 1
		n = numpy.random.randint(100)
		T.insert(n)
		nums.append(n)

	print T.inOrder()

	for n in nums:
		T.delete(n)
		print T.inOrder()