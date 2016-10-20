class element(object):
	
	def __init__(self,value):
		self.value 	= value
		self.next 	= None

class queue(object):
	def __init__(self,max_size=None):
		self._name 			= None
		self._first 		= None
		self._last 			= None
		self.max_size 		= max_size
		self.size 			= 0

	def is_empty(self):
		return (self.size == 0)

	def enqueue(self,item):
		new_item			= element(item)

		if self.is_empty():
			self._first 	= new_item
			self._last 		= new_item
		else:
			if self.size < self.max_size:
				self._last.next = new_item
				self._last 		= new_item
		self.size+=1

	def dequeue(self):
		if not self.is_empty():
			if self.size == 1:
				deq 		= self.first
				self._first  = None
				self._last 	= None
				return deq.value
			else:
				deq 			= self._first
				self._first 	= self._first.next
				return deq.value
		else:
			raise Exception('Queue Empty')

	def items(self):
		items 	= []
		current = self._first
		while current:
			items.append(current.value)
			current = current.next
		return items

if __name__ == '__main__':

	pass