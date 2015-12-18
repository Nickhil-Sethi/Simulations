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

def queue_simulation(simulation_time, append_probability = .1):
	q = queue()
	time = 0
	while(time <= simulation_time):
		v = numpy.random.rand()
		if v > append_probability:
			new_element = element(v)
			q.append(new_element)
		print q.last.value
		#############
		## service ##
		#  of Queue #
		#############
		time += 1

	return q


a = element(5)

queue_simulation(400)

