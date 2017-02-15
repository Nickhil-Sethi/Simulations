class Node(object):
	def __init__(self,value):
		self.value = value
		self.next  = None

	def __repr__(self):
		return "Linked List Node with Value {}".format(self.value)

class LinkedList(object):
	def __init__(self,vals=None):
		self.head = None
		self.tail = None
		self.size = 0
		if vals:
			for val in vals:
				self.append(val)

	def append(self,value):
		if not self.head:
			self.head      = Node(value)
			self.tail      = self.head
			self.size      = 1
		else:
			new            = Node(value)
			self.tail.next = new
			self.tail      = new
			self.size     += 1

	def getValues(self):
		vals    = []
		current = self.head
		while current:
			vals.append(current.value)
			current = current.next
		return vals

	def pop(self):
		nLast = self[self.size-2]

	def __getitem__(self,pos):

		if pos >= self.size:
			raise IndexError('index %d out of range' % pos)

		counter      = 0
		current      = self.head 
		while counter < pos:
			current  = current.next
			counter += 1
		return current

	def swap(self,node,prev):

		if not node.next:
			return
		newNext        = node.next.next
		prev.next      = node.next
		prev.next.next = node
		node.next      = newNext
		return node

	def swapPairs(self):
		prev              = None
		current           = self.head
		while current:
			if current is self.head:
				L         = current
				R         = current.next
				N         = current.next.next
				self.head = R
				R.next    = L
				L.next    = N			
				prev      = L
				current   = N
			else:
				prev      = self.swap(current,prev)
				current   = prev.next
		return self.head

	def reverse_in_K_groups(self,k):
		
		begin   = None
		end     = None
		current = self.head
		while current:
			
			stack   = []
			while current and len(stack) < k:
				stack.append(current)
				current = current.next

			if len(stack) < k:
				return self.head
			
			# reversed string will connect to end
			end     = current
			prev    = None
			while stack:
				n = stack.pop()
				if prev:
					prev.next = n
				else:
					first = n
				prev  = n

			# begin connects to string
			if not begin:
				self.head    = first
			else:
				begin.next   = first
			prev.next        = end 
			begin            = prev

if __name__=='__main__':
	L = LinkedList(range(10))
	print L.getValues()
	L.reverse_in_K_groups(3)
	print L.getValues()