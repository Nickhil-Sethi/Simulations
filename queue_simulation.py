import queue 

import numpy as np

class server(object):
	def __init__(self,inbuf_size,fail_probability):
		self.inbuf 				= queue.queue(max_size=inbuf_size)
		self.fail_probability 	= fail_probability
		self.active 			= True

	def process(self):
		if self.inbuf:
			p = self.inbuf.pop()

class service_network(object):
	def __init__(self):
		self.adj = {}


if __name__=='__main__':
	lam				= 20.0
	ENTRY_PROB		= .01
	FAIL_PROB 		= .1
	NUM_SERVERS 	= 10
	NUM_ENTRANTS	= 100
	SIM_TIME		= 4000

	def tree_like():
		
		SERVERS 		= [ server(np.random.randint(10),FAIL_PROB) for x in xrange(NUM_SERVERS) ]
		ENTRY			= queue.queue(max_size=100)
		
		t = 0
		while t < SIM_TIME:
			
			news = np.random.poisson(lam=lam)
			for i in xrange(news):
				ENTRY.enqueue(np.random.randint(20))

			for server in SERVERS:
				if server.active:
					try:
						server.inbuf.enqueue(ENTRY.dequeue())
					except Exception:
						pass
				if np.random.rand() <= server.fail_probability:
					server.active = False
				
			t += 1

		print([(server.inbuf.items(),server.active) for server in SERVERS])