class binary_node(object):
	def __init__(self,key,value=None):
		self.key = key
		self.value = value

		self.left = None
		self.right = None
		self.parent = None

	def children(self):

		ch = []
		if self.left:
			ch.append(self.left)
		if self.right:
			ch.append(self.right)

		return ch

	def insert(self,new_node):
		if not isinstance(new_node,binary_node):
			raise TypeError('new node must be instance of binary_node')

		current = self

		while current:
			
			prev = current

			if current.key <= new_node.key:
				current = current.right
			else:
				current = current.left

		new_node.parent = prev

		if prev.key <= new_node.key:
			prev.right = new_node
		else:
			prev.left = new_node

	# returns set of elements that have index 'search_index'
	def search(self,search_index):

		results = []

		current = self

		found = False
		while current:

			if current.index == search_index:
				results.append(current)
				current = current.right
			elif current.index < search_index:
				current = current.right
			else:
				current = current.left

		return results

	def deleteNode(self,delete_node):

		if not delete_node.children():
			
			parent = delete_node.parent
			
			if parent.right is delete_node:
				parent.right = None
			else:
				parent.left = None

			delete_node.parent = None

			return None

		elif len(delete_node.children()) == 1:

			parent = delete_node.parent

			if parent.right is delete_node:
				parent.right = delete_node.children()[0]
			else:
				parent.left = delete_node.children()[0]

			delete_node.children()[0].parent = parent

			return delete_node.children()[0]

		else:

			# find min
			current = delete_node.right

			while current:
				minRight = current
				current = current.left

			parent = delete_node.parent
			
			# assign minRights pointers to delete_nodes pointers
			minRight.parent = parent
			minRight.left = delete_node.left
			minRight.right = delete_node.right

			# children's parents point to minRight
			for child in delete_node.children():
				child.parent = minRight

			# delete delete_node's pointers
			delete_node.parent = None
			delete_node.right = None
			delete_node.left = None

			return minRight

	# delete all nodes that have index 'delete_index'
	def delete(self,delete_index):

		delete_nodes = self.search(delete_index)

		for node in delete_nodes:
			self.deleteNode(node)

	def inOrder(self):

		current = self

		res = []
		stack = []

		stack.append(current)

		while stack:

			while current:
				
				stack.append(current)
				current = current.left

			while stack:
				current = stack.pop()
				res.append((current.key,current.value))
				if current.right:
					current = current.right
					break
		return res



class binary_tree(object):

	def __init__(self):
		self.root = None
		self.size = 0

	def insert(self,node):
		if not isinstance(node,binary_node):
			raise TypeError('insert node must be instance of binary_node')
		if not self.root:
			self.root = node
		else:
			self.root.insert(node)
		self.size += 1

	def search(self,search_index):

		if not self.root:

			return []
		else:
			return self.root.search(search_index)

	def delete(self,delete_index):

		if self.root:

			delete_nodes = self.root.search(search_index)

			for node in delete_nodes:
				
				new = self.root.deleteNode(node)
				
				if not new.parent:
					self.root = new

			self.size -= 1
if __name__=='__main__':

	import numpy as np 

	B = binary_tree()

	while B.size < 100:
		B.insert( binary_node( (-1)**B.size*np.random.randint(1000) ) )

	print B.root.inOrder()

