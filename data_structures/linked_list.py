class element(object):
	def __init__(self,value):
		self.value 	= value
		self.next	= None
		self.prev 	= None


class DoublyLinkedList(object):

	def is_empty(self):
		return (self.length==0)

	def insert(self,item,pos=0):
		
		elem=element(item)

		if self.is_empty():
			self.head	= elem
			self.tail 	= elem
		else:
			self.tail.next 	= elem
			elem.prev 		= self.tail
			self.tail		= elem

		self.length 		+= 1 
	
	def __init__(self,elems=None):
		if elems and not type(elems) is list:
			raise TypeError('DoublyLinkedList initializer expects type list')
		self.head = None
		self.tail = None
		self.length=0
		if elems:
			for element in elems:
				self.insert(element)

	def pop(self):
		if self.is_empty():
			raise Exception('List is empty')
		elif self.length == 1:
			old_tail 		= self.tail
			self.head 		= None
			self.tail 		= None
			self.length 	-= 1
			return old_tail
		else:
			new_tail 		= self.tail.prev
			old_tail 		= self.tail
			new_tail.next 	= None
			self.tail 		= new_tail
			self.length 	-= 1
			return old_tail
	def __getitem__(self,index):
		if index > self.length-1:
			raise IndexError('%d th element does not exist' % index)

		counter = 0
		current = self.head
		while counter <= index:
			current = current.next
			counter += 1
		return current

class OrderedMap(DoublyLinkedList):
	def __init__(self,items=None):
		if items:
			for item in items:
				assert len(item) == 2

		self.list = DoublyLinkedList()
		self.map  = {}

		if items:
			for item in items:
				self.list.insert(item)
				self.map[item[0]] = self.list[]


if __name__ == '__main__':

	DL = DoublyLinkedList(['a','b','c'])
	while not DL.is_empty():
		print(DL.pop().value)
