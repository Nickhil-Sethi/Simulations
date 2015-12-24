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
		if not isinstance(el, element):
			raise TypeError('Not Correct Class!')
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
		

def find_server(server_dict):
	#returns first server which is active
	l = len(server_dict)
	if not isinstance(server_dict[0], server):
		raise TypeError('Not a server!')
	else:
		for s in range(l):
			serv = server_dict[s]
			if serv.active == True:
				return serv
		print 'No active servers'
		return -1

def queue_simulation(simulation_time = 400, service_start = 10, num_servers = 1, arrival_probability = .3, f_prob = .01):
	
	time = 0
	service_counter = 0

	q = queue()
	serv_dict = {}
	for i in range(num_servers):
		serv_dict[i] = server(failure_probability = f_prob)

	print 'failure probability = ', serv_dict[0].failure_probability, '\n'

	while(time <= simulation_time):
		#random arrival at end of queue

		servers_active = float(sum([serv_dict[i].active == True for i in range(num_servers)]))/(float(num_servers))

		if servers_active == 0.0:
			print '0% of original {} server(s) still active. ending simulation at time {}'.format(num_servers,time)
			return time

		print 'percent of servers still active = {}%'.format(servers_active*100)
		v = numpy.random.rand()
		if v > arrival_probability:
			new_element = element(service_counter)
			q.append(new_element)

		#randomly deactivate servers; servers go down, but do not come back up
		for k in range(num_servers):
			serv = serv_dict[k]
			f = numpy.random.rand()
			if f < serv.failure_probability:
				print 'crash occurred in server {}'.format(k)
				serv.active = False 

		#service starts
		n = q.pop()
		if n != -1:
			first_server = find_server(serv_dict)
			if isinstance(first_server, server):
			#bug here! first_server is "NoneType"
				first_server.service(n)
				print 'current queue length', q.len
			
		print 
		service_counter += 1
		time += 1

	return q

s = server()
print s.failure_probability
queue_simulation(num_servers = 10)
