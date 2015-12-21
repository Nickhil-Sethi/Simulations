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
			return -1
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
		self.active = True 
	def service(self, customer):
		if(not isinstance(customer,element)):
			print customer, type(customer)
			raise TypeError('Not an element of queue!')
		else:
			print customer.value, 'serviced'
		return

def find_server(server_dict):
	#returns first server which is active
	if not isinstance(server_dict[0], server):
		raise TypeError('Not a server!')
	else:
		for server in server_dict:
			if server.active == True:
				return server

def queue_simulation(simulation_time = 40, service_start = 10, num_servers = 1, arrival_probability = .3, failure_probability = .01):
	time = 0

	q = queue()
	server_dict = {}
	for i in range(num_servers):
		server_dict[i] = server(failure_probability)
	print 'failure probability = ', server_dict[0].failure_probability, '\n'

	while(time <= simulation_time):
		#random arrival at end of queue 
		v = numpy.random.rand()
		if v > arrival_probability:
			new_element = element(v)
			q.append(new_element)

		#randomly deactivate servers; servers go down, but do not come back up
		for server in server_dict:
			f = numpy.random.rand()
			if f < server.failure_probability:
				server.active = False 

		#service starts
		n = q.pop()
		if n != -1:
			first_server = find_server(server_dict)
			first_server.service(n)
			print q.len
	
		time += 1

	return q

queue_simulation(failure_probability = .5)
