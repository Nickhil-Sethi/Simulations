class element(object):
	def __init__(self,value):
		self.value = value
		self.next = None

	def __repr__(self):
		return "stack element; value {}".format(self.value)

class stack(object):
	def __init__(self):
		self.top = None
		self.size = 0

	def is_empty(self):
		if self.size != 0:
			return False
		else:
			return True

	def push(self,a):
		element_a = element(a)
		element_a.next=self.top
		self.top=element_a
		self.size += 1

	def pop(self):
		if not self.is_empty():
			popped = self.top.value
			self.top = self.top.next
			self.size -= 1
			return popped
		else:
			raise ValueError('Stack Empty!')

if __name__ == '__main__':
	
	s = stack()
		
	for i in xrange(100):
		s.push(i)

	print "size = ", s.size, "\n"

	print s.top
	s.print_stack()

	while not s.is_empty():
		print "pop ", s.pop()

	print "size = ", s.size
