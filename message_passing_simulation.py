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
	return adj

class server(object):
	def __init__(self,sid,adj):
		if not type(adj) is dict:
			raise TypeError('server object must receive dictionary for adj')
		self.sid = sid
		self.children = list(adj[self.sid])
		self.parents = list(set([k for k in adj if self.sid in adj[k]]))
		if self.parents:
			self.inbuf = {}
			for p in self.parents:
				self.inbuf[p] = 'null'
		else:
			self.inbuf = None
		if self.children:
			self.outbuf = {}
			for c in self.children:
				self.outbuf[c] = 'null'
		else:
			self.outbuf = None
		self.terminated = False
		self.state = [self.inbuf,self.outbuf,self.terminated]

	def comp(self,serv_dict):
		print "server {} computing".format(self.sid)
		for p in self.parents:
			#print "children of {}: {}".format(p, serv_dict[p].children), "outbuf of {}: {}".format(p, serv_dict[p].outbuf)
			if serv_dict[p].outbuf[self.sid] != None:
				self.inbuf[p] = (serv_dict[p]).outbuf[self.sid]
		if 'm' in [self.inbuf[i] for i in self.parents]:
			for i in self.children:
				self.outbuf[i] = 'm'
			self.terminated = True

		return
	def comp_random1(self,serv_dict):
		#print "server {} computing".format(self.sid)
		for p in self.parents:
			#print "children of {}: {}".format(p, serv_dict[p].children), "outbuf of {}: {}".format(p, serv_dict[p].outbuf)
			if serv_dict[p].outbuf[self.sid] != None:
				self.inbuf[p] = (serv_dict[p]).outbuf[self.sid]
		if 'm' in [self.inbuf[i] for i in self.parents]:
			if self.children:
				l = len(self.children)
				r = np.random.random_integers(0,l-1)
				self.outbuf[self.children[r]] = 'm'
				self.terminated = True
				print "server {} sent message to server {}".format(self.sid,self.children[r])
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

	#number of servers (nodes) extracted from adj
	n = len(adj)
	print "number of nodes = {}".format(n)

	#constructing dictionary of servers
	serv_dict = {}
	for k in adj:
		serv_dict[k] = server(k,adj)

	#initializing root server with message on all outgoing channels
	print serv_dict[0].children, serv_dict[0].parents, serv_dict[0].outbuf
	for k in serv_dict[0].children:
		serv_dict[0].outbuf[k] = 'm'

	print serv_dict[1].outbuf
	#begin simulation
	time = 0
	while time <= sim_time and keep_going(serv_dict):
		for k in serv_dict:
			#serv_dict[k].comp(serv_dict)
			serv_dict[k].comp_random1(serv_dict)
		
		if 'm' in [serv_dict[n-1].inbuf[k] for k in serv_dict[n-1].parents]:
			print 'success!'
			return

		time += 1
	print 'fail! simulation ended at time {}'.format(time)
	return 


adj = construct_random_graph_asymmetric(N,.5)
print adj

message_pass_deterministic(adj,N*N)

