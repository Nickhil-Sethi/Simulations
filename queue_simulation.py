import sys
sys.path.insert(0,'/Library/Python/2.7/site-packages')

import os
import sys
import timeit

import numpy

class element(object):
	def __init__(self, value):
		self.value = value
		self.next = 'null'
		self.before = 'null'

class queue(object):
	def __init__(self):
		self.len = 0
		self.first = element('null')
		self.last = element('null')

	def pop(self):
		if self.len==0:
			print 'queue empty'
			return
		elif self.len == 1:
			r  = self.first
			self.first = 'null'
			self.len = 0
			return r
		else:
			print self.len, self.first.value
			r = self.first
			self.first = self.first.next
			self.len = self.len - 1
			return r

	def append(self,el):
		#if type(el != element):
		#	raise TypeError('Not Correct Class!')
		if self.len == 0:
			self.first = el
			self.last = el
			self.len += 1
		else:
			self.last.next = el
			self.last = el
			self.len += 1

	def get_next(self,el):
		return el.next.value

	def get_element(self,a):
		#linear search for a'th element in queue
		if type(a) != int:
			raise TypeError('Index must be integer!')
		elif a < 0:
			raise TypeError('a must be greater than 0')

		elif a > self.len:
			raise TypeError('Index is greater than length of queue')
		else:
			counter = 0
			current = self.first
			while(counter <= a and counter <= self.len):
				if(counter == a):
					return current.value
				current = current.next
				counter += 1

class server(object):
	def __init__(self, failure_probability = .01):
		self.failure_probability = failure_probability
	def service(self, customer):
		if(not isinstance(customer,element)):
			print customer, type(customer)
			raise TypeError('Not an element of queue!')
		else:
			print customer.value, 'serviced'
		return

def queue_simulation(simulation_time = 40, service_start = 10, arrival_probability = .3, failure_probability = .01):
	time = 0

	q = queue()
	s = server(failure_probability)
	print 'failure probability = ', s.failure_probability, '\n'

	while(time <= simulation_time):
		#loading queue before service starts
		if time < service_start:
			v = numpy.random.rand()
			if v > arrival_probability:
				new_element = element(v)
				q.append(new_element)

		#service starts
		else:
			f = numpy.random.rand()
			v = numpy.random.rand()
			if v > arrival_probability:
				new_element = element(v)
				q.append(new_element)
			n = q.pop()
			if q.len > 0 and f > s.failure_probability:
				s.service(n)
				print q.len
			elif f <= s.failure_probability:
				print 'crash at time %d' %(time)
		
		time += 1

	return q

queue_simulation(failure_probability = .5)
