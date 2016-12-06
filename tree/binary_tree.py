""" binaryNode class """

class binaryNode(object):
	def __init__(self,key,value=None):
		self.key 			= key
		self.value 			= value
		self.left 			= None
		self.right 			= None
		self.parent			= None
		self.size 			= 1

	def min_right(self):
		parent 				= None
		prev 				= self
		current 			= self.right
		while current:
			parent 			= prev
			prev 			= current
			current 		= current.left
		return prev, parent
	
	def is_right(self):
		return (self.parent != None and self.parent.key < self.key)

	def set_left(self,node):
		self.left 			= node
		node.parent 		= self

	def set_right(self,node):
		self.right  		= node
		node.parent 		= self

	def insert(self,key,value=None):

		newNode 			= binaryNode(key,value)
		current 			= self
		while current:
			if current.key == key:
				current.value = value
				return
			prev 			= current
			if current.key < key:
				current 	= current.right
			else:
				current 	= current.left

		if prev.key < key:
			prev.set_right(newNode)
		else:
			prev.set_left(newNode)

	def search(self,key):
		prev    = None
		current = self
		while current:
			if current.key == key:
				return current
			prev = current
			if current.key < key:
				current 	= current.right
			else:
				current		= current.left
		return current

	def isSorted(self,arr):
		for i in xrange(len(arr)-1):
			if arr[i] > arr[i+1]:
				return False
		return True

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
					# print "st", current
					ret.append(current)
					if current.right:
						current = current.right
						stack.append(current)
						break
		return ret

	def delete(self,key):
		node = self.search(key)
		if node != None and node != self:
			parent = node.parent
			if not node.left and not node.right:
				if parent.key < node.key:
					parent.right = None
				else:
					parent.left  = None
				del node
				return
			if node.left and not node.right:
				if parent.key < node.key:
					parent.set_right(node.left)
				else:
					parent.set_left(node.left)
				node.left        = None
				del node
				return
			if node.right and not node.left:
				if parent.key < node.key:
					parent.set_right(node.right)
				else:
					parent.set_left(node.right)
				node.right 	     	 = None
				del node
				return
			if node.right and node.left:
				minRight, Rparent = node.min_right()
				if minRight == node.right:
					if parent.key < node.key:
						parent.set_right(minRight)
					else:
						parent.set_left(minRight)
					minRight.set_left(node.left)
					node.left 		 	 = None
					node.right       	 = None
				else:
					if minRight.right:
						Rparent.set_left(minRight.right)
						minRight.right  = None
					else:
						Rparent.left    = None

					if parent.key < node.key:
						parent.set_right(minRight)
					else:
						parent.set_left(minRight)
					
					minRight.set_left(node.left)
					minRight.set_right(node.right)

				del node
				return

	def __contains__(self,key):
		return (self.search(key) != None)

	def __repr__(self):
		return "key {}".format(self.key,self.value)





""" AVLnode class """
class AVLnode(binaryNode):
	def __init__(self,key,value=None):
		binaryNode.__init__(self,key,value)
		self.height         = 1
	
	def is_balanced(self):
		if -2 < self.balance_factor() < 2:
			if self.left and self.right:
				return self.left.is_balanced() and self.right.is_balanced()
			elif self.left:
				return self.left.is_balanced()
			elif self.right:
				return self.right.is_balanced()
			else:
				return True
		return False

	def balance_factor(self):
		lh = 0
		if self.left:
			lh = self.left.height
		rh = 0
		if self.right:
			rh = self.right.height
		return rh - lh

	def get_height(self):
		if not self.left and not self.right:
			self.height = 1
			return 1
		else:
			l_height = 0
			if self.left:
				l_height = self.left.height
			
			r_height = 0
			if self.right:
				r_height = self.right.height

			self.height  = 1 + max(l_height,r_height)
			return self.height

	def rotate_left(self):
		if not self.right:
			return
		P 				= self.parent
		R 				= self.right

		self.right  	= R.left
		if R.left:
			R.left.parent 	= self	
		
		R.set_left(self)

		if P and P.key < self.key:
			P.set_right(R)
		elif P:
			P.set_left(R)
		else:
			R.parent = None
		
		self.get_height()
		R.get_height()
		return R

	def rotate_right(self):
		if not self.left:
			return
		P 				= self.parent
		L 				= self.left

		self.left 		= L.right
		if L.right:
			L.right.parent 	= self
		
		L.set_right(self)
		
		if P and P.key < self.key:
			P.set_right(L)
		elif P:
			P.set_left(L)
		else:
			L.parent = None

		self.get_height()
		L.get_height()
		return L

	def insert(self,key,value=None):

		newNode = AVLnode(key,value)
		stack   = []
		current = self
		prev    = None

		while current:
			if current.key == key:
				current.value = value
				return
			stack.append(current)
			prev    	= current
			if current.key < key:
				current = current.right
			else:
				current = current.left

		if prev.key < key:
			prev.set_right(newNode)
		else:
			prev.set_left(newNode)
		stack.append(newNode)
		self.size += 1

		# rebalancing tree
		newRoot = None
		while stack:
			current 		= stack.pop()
			current.get_height()
			if current.balance_factor() > 1:
				if not current.balance_factor() == 2:
					raise ValueError('{} balance factor == {}; trying to insert {}'.format(current,current.balance_factor(),newNode))
				if current.right.right and key in current.right.right:
					current 					 = current.rotate_left()
				else:
					current.right 				 = current.right.rotate_right()
					current      				 = current.rotate_left()
				if not current.parent:
					newRoot = current
				break
			elif current.balance_factor() < -1:
				if not current.balance_factor() == -2:
					raise ValueError('{} balance factor == {}; trying to insert {}'.format(current,current.balance_factor(),newNode))
				if current.left.left and key in current.left.left:
					current 					 = current.rotate_right()
				else:
					current.left 				 = current.left.rotate_left()
					current						 = current.rotate_right()
				if not current.parent:
					newRoot = current
				break
		# adjust balance_factors for other nodes
		while stack:
			current = stack.pop() 
			current.get_height()

		return newRoot

	def delete(self,key):
		node  = self.search(key)
		if node != None and node != self:
			Found = True
			if not node.left and not node.right:
				if node.is_right():
					node.parent.right = None
				else:
					node.parent.left  = None
				
				current = node.parent
				while current:
					current.get_height()
					current = current.parent
				
				del node
				self.size -= 1
				return
			if node.left and not node.right:
				if node.is_right():
					node.parent.set_right(node.left)
				else:
					node.parent.set_left(node.left)

				current = node.parent
				while current:
					current.get_height()
					current = current.parent

				del node
				self.size -= 1
				return
			if node.right and not node.left:
				if node.is_right():
					node.parent.set_right(node.right)
				else:
					node.parent.set_left(node.right)

				current = node.parent
				while current:
					current.get_height()
					current = current.parent

				del node
				self.size -= 1
				return
			if node.right and node.left:
				minRight, Rparent = node.min_right()
				if node.right == minRight:
					if node.is_right():
						node.parent.set_right(node.right)
					else:
						node.parent.set_left(node.right)
					node.right.set_left(node.left)
					current = node.right
					while current:
						current.get_height()
						current = current.parent
					del node
					self.size -= 1
					return
				else:
					if minRight.right:
						minRight.parent.set_left(minRight.right)
					else:
						minRight.parent.left = None
					if node.is_right():
						node.parent.set_right(minRight)
					else:
						node.parent.set_left(minRight)
					minRight.set_left(node.left)
					minRight.set_right(node.right)

					current = node.parent
					while current:
						current.get_height()
						current = current.parent
					del node
					self.size -= 1
					return

class AVLTree(object):
	def __init__(self,values=None):
		self.root = None
		if values:
			assert type(values) is list
			for value in values:
				self.insert(value[0],value[1])
	
	def size(self):
		if not self.root:
			return 0
		return self.root.size
		
	def insert(self,key,value=None):
		if not self.root:
			self.root = AVLnode(key,value)
		else:
			v = self.root.insert(key,value)
			if v:
				self.root = v

	def delete(self,key):
		if self.root:
			self.root.delete(key)

	
	def search(self,key):
		if self.root:
			return self.root.search(key)
		else:
			return None
	
	def inOrder(self):
		if not self.root:
			return []
		else:
			return self.root.inOrder()

	def is_balanced(self):
		if self.root:
			return self.root.is_balanced()
		return True

if __name__=='__main__':

	import numpy as np

	test_AVL = True
	if test_AVL:
		n  = AVLTree()
		c  = 0
		ins = []
		while c < 1000:
			c += 1
			num = np.random.randint(100)
			ins.append(num)
			n.insert(num)
		print n.root.is_balanced()

		for num in ins:
			n.delete(num)
			print n.is_balanced()

	if not test_AVL:
		b = binaryNode(5)
		c = 0 
		while c < 100:
			c += 1
			num = np.random.randint(100)
			b.insert(num)
			print [i.key for i in b.inOrder()]
