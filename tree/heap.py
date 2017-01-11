from collections import deque

class MinHeap(object):
	def __init__(self,vals=None):		
		self.vals = [] if vals is None else vals
		for i in xrange(len(self.vals)-2//2,-1,-1):
			self.heapify_down(i)
	
	def min_child(self,k):
		if 2*k+1 >= len(self.vals):
			return None
		if 2*k+2 < len(self.vals):
			if  self.vals[2*k+1] < self.vals[2*k+2]:
				return 2*k + 1
			else:
				return 2*k + 2
		return 2*k + 1
	
	def heapify_down(self,k):
		m = self.min_child(k)
		if m is None:
			return None
		if self.vals[m] < self.vals[k]:
			self.vals[m], self.vals[k] = self.vals[k], self.vals[m]
			self.heapify_down(m)

	def heapify_up(self,k):
		if k == 0:
			return
		if (k-1)//2 >= 0 and self.vals[(k-1)//2] > self.vals[k]:
			self.vals[(k-1)//2], self.vals[k] = self.vals[k], self.vals[(k-1)//2]
			self.heapify_up((k-1)//2)

	def insert(self,val):
		self.vals.append(val)
		self.heapify_up(len(self.vals)-1)

	def delete(self):
		if len(self.vals) == 1:
			return self.vals.pop()
		ret          = self.vals[0]
		self.vals[0] = self.vals.pop()
		self.heapify_down(0)
		return ret

	def verify(self,k):
		if 2*k+1 >= len(self.vals):
			return True
		
		if 2*k+2 < len(self.vals):
			if self.vals[k] > self.vals[2*k+1] or self.vals[k] > self.vals[2*k+2]:
				return False
			else:
				return self.verify(2*k+1) and self.verify(2*k+2)
		if 2*k+1 < len(self.vals):
			if self.vals[k] > self.vals[2*k+1]:
				return False
			else:
				return self.verify(2*k+1)

	def isHeap(self):
		return self.verify(0)

	def find_less_than(self,k):
		ret   = []
		queue = deque()
		queue.appendleft(0)
		while queue:
			current = queue.popleft()
			if self.vals[current] < k:
				ret.append(self.vals[current])
				if 2*current + 2 < len(self.vals):
					queue.appendleft(2*current+1)
					queue.appendleft(2*current+2)
				elif 2*current + 1 < len(self.vals):
					queue.appendleft(2*current+1)
		return ret

	def find_kth_smallest(self,k):
		catch = []
		for i in xrange(k):
			catch.append(self.delete())
		ret = self.vals[0]
		for c in catch:
			self.insert(c)
		return ret

	def merge(self,secondHeap):
		self.vals = self.vals + secondHeap.vals
		for i in xrange(len(self.vals)-2//2,-1,-1):
			self.heapify_down(i)

if __name__=='__main__':
	import numpy as np
	a = [np.random.randint(100) for i in xrange(200)]
	h = MinHeap(a)
	print h.find_less_than(200)
	print h.isHeap()