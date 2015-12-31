import sys
sys.path.insert(0,'/Library/Python/2.7/site-packages')

import os
import sys
import time
import timeit

import numpy as np

N = 10

def construct_random_graph_asymmetric(N, delta):
	#induces a simple partial order on nodes
	adj = {}
	for i in range(N):
		adj[i] = set()
		for j in range(i+1,N):
			if(np.random.rand() < delta):
				adj[i].add(j)
	#for i in range(N):
	#	adj[i] = list(adj[i])
	return adj

class server(object):
	def __init__(self,sid,adj):
		if not type(adj) is dict:
			raise TypeError('server object must receive dictionary for adj')
		self.sid = sid
		self.inbuf = {}
		self.outbuf = {}
		self.children = set(adj[self.sid])
		self.parents = set([k for k in adj if self.sid in adj[k]])
		self.terminated = False
		self.state = [self.inbuf,self.outbuf,self.terminated]

	def comp(self,serv_dict):
		for p in self.parents:
			print p, serv_dict[self.sid].children
			self.inbuf[p] = serv_dict[p].outbuf[self.sid]
		if 'm' in [self.inbuf[i] for i in self.parents]:
			for i in self.children:
				self.outbuf[i] = 'm'
			self.terminated = True
		'''
		for j in self.inbuf():
			if self.inbuf[j] == 'm':
				for i in self.children:
					self.outbuf[i] = 'm'
				return
		'''
		return

def keep_going(serv_dict):
	#checks if there is still a server running
	if not type(serv_dict) is dict:
		raise TypeError('must be dictionary')
	#does this search faster than 'if True in [serv_dict[k].terminated for k in serv_dict]'?
	for k in serv_dict:
		if serv_dict[k].terminated == False:
			return True 
	return False

def message_pass_deterministic(adj,sim_time):
	n = len(adj)
	serv_dict = {}
	for k in adj:
		serv_dict[k] = server(k,adj)

	#initializing root server with message on all outgoing channels
	for k in serv_dict[0].children:
		serv_dict[0].outbuf[k] = 'm'

	time = 0
	while time <= sim_time and keep_going(serv_dict):
		for k in serv_dict:
			print k
			serv_dict[k].comp(serv_dict)
		time += 1
		if 'm' in [serv_dict[n].inbuf[k] for k in serv_dict[n].parents]:
			print 'success!'
	return 
def message_pass_random(adj,sim_time):
	fdasf
	return False 


adj = construct_random_graph_asymmetric(N,.5)
print adj
message_pass_deterministic(adj,N+1)