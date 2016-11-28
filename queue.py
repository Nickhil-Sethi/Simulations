class element(object):
	
	def __init__(self,value):
		self.value = value
		self.next = None

	def __repr__(self):
		return "queue element; value {} ".format(self.value)

class queue(object):
	def __init__(self):
		self.name = None
		self.first = None
		self.last = None
		self.size = 0

	def __repr__(self):
		#return "[queue : name {} : size {}]".format(self.name, self.size())
		return "queue {}".format(self.name)

	def is_empty(self):
		return (self.size == 0)

	def enqueue(self,item):
		new_item=element(item)
		if self.is_empty():
			self.first = new_item
			self.last = new_item
		else:
			self.last.next = new_item
			self.last = new_item
			
		self.size+=1

	def dequeue(self):
		if not self.is_empty():
			if self.size == 1:
				self.size -= 1
				return self.first.value
			else:
				deq=self.first
				self.first = self.first.next
				self.size -= 1
				return deq.value
		else:
			raise ValueError('queue empty!')

	def first():
		return self.first.value
if __name__ == '__main__':

	import numpy as np 

	time = 0
	sim_time = 100
	begin_at = 50
	arrival_probability = .56
	q=queue()

	while time <= sim_time:
		new=np.random.rand()
		if new < arrival_probability:
			q.enqueue(new)

		if time >= begin_at:
			try:
				print q.dequeue()
			except ValueError:
				print "end"
				break

		time += 1 
