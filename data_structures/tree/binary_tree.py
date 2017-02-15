"""Implementation of a binaryNode, AVLNode, and AVLTree objects"""

class binaryNode(object):
	def __init__(self,key,value=None):
		self.key 			= key
		self.value 			= value
		self.left 			= None
		self.right 			= None
		self.parent			= None
		self.size 			= 1

	def min_right(self):
		prev 				= self
		current 			= self.right
		while current:
			prev 			= current
			current 		= current.left
		return prev

	def is_right(self):
		return (self.parent != None and self.parent.key < self.key)

	def set_left(self,node):
		if node is None:
			self.left = None
			return
		self.left 			= node
		node.parent 		= self

	def set_right(self,node):
		if node is None:
			self.right = None
			return
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
		self.size += 1

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
					ret.append(current)
					if current.right:
						current = current.right
						stack.append(current)
						break
		return ret

	def delete(self,key):
		node = self.search(key)
		if node != None and node != self:
			self.size -= 1
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
				minRight = node.min_right()
				Rparent  = minRight.parent
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

class AVLnode(binaryNode):
	def __init__(self,key,value=None):
		binaryNode.__init__(self,key,value)
		self.balance_factor = 0
		self.height         = 1
		self.size 			= 1
	
	def adjust_balance_factor(self):
		left_height 		= self.left.height if self.left else 0
		right_height 		= self.right.height if self.right else 0
		self.balance_factor = right_height - left_height
		return self.balance_factor

	def adjust_height(self):
		left_height 		= self.left.height if self.left else 0
		right_height 		= self.right.height if self.right else 0
		self.height 		= 1 + max(left_height,right_height)
		return self.height

	def adjust_size(self):
		left_size 			= self.left.size if self.left else 0
		right_size 			= self.right.size if self.right else 0
		self.size 			= 1 + left_size + right_size
		return self.size 
	
	def rotate_left(self):
		if not self.right:
			raise Exception('right not present; {} only has {}'.format(self.key,self.inOrder()))

		P 					= self.parent
		R 					= self.right

		self.set_right(R.left)
		R.set_left(self)

		if P and P.key < self.key:
			P.set_right(R)
		elif P:
			P.set_left(R)
		else:
			R.parent = None

		self.adjust_size()
		self.adjust_height()
		self.adjust_balance_factor()

		R.adjust_size()
		R.adjust_height()
		R.adjust_balance_factor()

		if P:
			P.adjust_size()
			P.adjust_height()
			P.adjust_balance_factor()

		return R

	def rotate_right(self):
		if not self.left:
			raise Exception('left not present; only has {}'.format(self.inOrder()))
		P 					= self.parent
		L 					= self.left

		self.set_left(L.right)
		L.set_right(self)

		if P and P.key < self.key:
			P.set_right(L)
		elif P:
			P.set_left(L)
		else:
			L.parent = None

		self.adjust_size()
		self.adjust_height()
		self.adjust_balance_factor()

		L.adjust_size()
		L.adjust_height()
		L.adjust_balance_factor()

		if P:
			P.adjust_size()
			P.adjust_height()
			P.adjust_balance_factor()

		return L

	def insert(self,key,value=None):
		newNode = AVLnode(key,value)
		stack   = []
		prev 	= None
		current = self

		while current:
			if current.key == key:
				current.value = value
				return
			stack.append(current)
			prev 	= current
			if current.key < key:
				current = current.right
			else:
				current = current.left

		if prev.key < key:
			prev.set_right(newNode)
		else:
			prev.set_left(newNode)

		stack.append(newNode)
		newRoot = None
		while stack:
			current = stack.pop()
			current.adjust_size()
			current.adjust_height()
			if current.adjust_balance_factor() > 1:
				assert current.balance_factor == 2
				if current.right.right and key in current.right.right:
					current 		= current.rotate_left()
				else:
					current.right 	= current.right.rotate_right()
					current		  	= current.rotate_left()
				if not current.parent:
					newRoot = current
			elif current.adjust_balance_factor() < -1:
				assert current.balance_factor == -2
				if current.left.left and key in current.left.left:
					current			= current.rotate_right()
				else:
					current.left 	= current.left.rotate_left()
					current			= current.rotate_right()
				if not current.parent:
					newRoot = current
		return newRoot

	def delete(self,key):
		node = self.search(key)
		if node and node is self:
			parent = node.parent
			if not node.left and not node.right:
				if node.is_right():
					parent.right = None
				else:
					parent.left  = None
				del node
				
				current = parent
				while current:
					current.adjust_size()
					current.adjust_height()
					current.adjust_balance_factor()
					current = current.parent
				return
			if node.left and not node.right:
				if node.is_right():
					parent.set_right(node.left)
				else:
					parent.set_left(node.left)

				current = parent 
				while current:
					current.adjust_size()
					current.adjust_height()
					current.adjust_balance_factor()
					current = current.parent
				return

			if node.right and not node.left:
				if node.is_right():
					parent.set_right(node.right)
				else:
					parent.set_left(node.right)

				current = parent
				while current:
					current.adjust_size()
					current.adjust_height()
					current.adjust_balance_factor()
					current = current.parent
				return
			if node.left and node.right:
				minRight = node.min_right()
				rParent  = minRight.Parent
				if minRight is node.right:
					minRight.set_left(node.left)
					if node.is_right():
						parent.set_right(minRight)
					else:
						parent.set_left(minRight)
				else:
					if minRight.right:
						rParent.set_left(minRight.right)
					else:
						rParent.left 	= None
					minRight.set_left(node.left)
					minRight.set_right(node.right)
					if node.is_right():
						parent.set_right(minRight)
					else:
						parent.set_left(minRight)

					current = rParent
					while current:
						current.adjust_size()
						current.adjust_height()
						current.adjust_balance_factor()
						current = current.parent

					return 

class AVLTree(object):
	def __init__(self):
		self.root = None

	def insert(self,key,value=None):
		if not self.root:
			self.root = AVLnode(key,value)
		else:
			newRoot = self.root.insert(key,value)
			if newRoot:
				self.root = newRoot

	def size(self):
		return self.root.size if self.root else 0

	def search(self,key):
		if not self.root:
			return None
		else:
			return self.root.search(key)

	def delete(self,key):
		if key != self.root.key:
			self.root.delete(key)
		else:
			# TODO : delete root case
			pass

	def inOrder(self):
		if not self.root:
			return []
		else:
			return self.root.inOrder()

	def __iter__(self):
		items = self.inOrder()
		for item in items:
			yield item

if __name__=='__main__':

	import numpy as np

	test_AVL = False
	if test_AVL:

		size = 100
		print "testing AVLTree object; generating random tree of size %d \n" % size 
		
		v = AVLTree()
		while v.size() < size :
			v.insert(np.random.randint(100))

		print "printing keys inOrder"
		print v.inOrder()

	test_binary = True
	if test_binary:
		sz = 100
		
		print "testing binaryNode object; inserting %d random nodes\n" % sz 
		b = binaryNode(5)
		while b.size < sz:
			num = np.random.randint(400)
			b.insert(num)

		print "printing node keys inOrder"
		print [i.key for i in b.inOrder()]
