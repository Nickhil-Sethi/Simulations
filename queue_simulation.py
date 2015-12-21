import sys
sys.path.insert(0,'/Library/Python/2.7/site-packages')

import os
import sys
import timeit

import numpy

import theano
import my_logistic_regression as lr 

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


def queue_simulation(simulation_time, arrival_probability = .1):


	clf = lr.sgd_optimization_mnist(n_epochs = 1)
	W,b = clf.W.get_value(),clf.b.get_value()

	predict = theano.function(
		inputs = [clf.input],
		outputs = [clf.y_pred],
		)

	rval = lr.load_data('/Users/Nickhil_Sethi/Documents/Datasets/mnist.pkl')
	train_set_x, train_set_y = rval[0]

	q = queue()
	time = 0
	
	while(time <= simulation_time):
		v = numpy.random.rand()
		if v > arrival_probability:
			new_element = element(train_set_x[time])
			q.append(new_element)
			predict(train_set_x[time])

		#############
		## service ##
		#  of Queue #
		#############
		
		time += 1

	return q

a = element(5)
queue_simulation(400)
