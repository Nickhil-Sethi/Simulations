class element(object):
	def __init__(self,value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None
	
	def children(self):
		children = {}
		if self.left:
			children['left'] = self.left
		if self.right:
			children['right'] = self.right
		return children

class heap(object):
	def  __init__(self,N):
		self.root = None
		self.end = None
		self.size = 0
		self.max_size = N
	
	def swap(self,parent,child):

		assert child == parent.left or child == parent.right
		was_left  		= (child == parent.left)
		was_right 		= (child == parent.right)

		new_parent 		= parent.parent
		child.parent 	= None

		new_children = child.children()
		if 'left' in new_children:
			parent.left = child.left
		if 'right' in new_children:
			parent.right = child.right

		if was_right:
			child.right = parent
		if was_left:
			 child.left = parent
		if new_parent:
			child.parent = new_parent

	def heapify_up(self, item):
		if not item.parent:
			return
		elif item.value > item.parent.value:
			return 
		else:
			self.swap(item.parent,item)
			self.heapify_up(item.parent)
		return
	
	def heapify_down(self,item):
		if not item.children():
			return
		elif not item.right:
			if item.value > item.left.value:
				self.swap(item,item.left)
				self.heapify_down(self.left)

		elif not item.left:
			if item.value > item.right.value:
				self.swap(item,item.right)
				self.heapify_down(item.right)
		else:
			if item.left.value > item.right.value:
				self.swap(item, item.right)
				self.heapify_down(self.right)
			else:
				self.swap(item,item.left)
				self.heapify_down(item.left)
		return
	
	def insert(self,item,pos=None):
		if pos and len(pos.children()) == 2:
			raise ValueError('must choose root node')
		if self.size == 0:
			self.root = item
			self.size += 1
		else:
			if pos.right:
				pos.left = item
			else:
				pos.right = item
			self.heapify_up(item)
			self.size += 1

if __name__ == '__main__':
	H = heap(3)
	H.insert(element(4))
	H.insert(element(2),H.root)
	print H.root.value, H.root.right.value
	H.heapify_down(H.root)

