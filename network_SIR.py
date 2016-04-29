# -*- coding: utf-8 -*-
"""
@author: Nickhil_Sethi

SIR simulation on network

"""
#from graph_tool.all import *
import numpy as np
from network import *
import queue

def simulation(N=100,time=100,graph='random',delta=.1, w=.5,p=.5,dt=.01,alpha_raw=1.0,beta_raw=1.0):

    # sanity checks
    graphs = ['random','scale free','small world']

    if not graph in graphs:
        raise ValueError('graph must be type [random, scale free, small world]')

    if not 0 <= delta <= 1:
        raise ValueError('delta must be in [0,1]')
    if not 0 <= w <= 1:
        raise ValueError('w must be in [0,1]')
    if not 0 <= p <= 1:
        raise ValueError('p must be in [0,1]')


    # constructing network
    if graph == 'random':
        adj = construct_random_graph(N,delta)
    elif graph == 'scale free':
        adj = construct_scale_free_graph(N,w)
    else:
        adj = construct_small_world_graph(N,p)

    # state transition probabilities for nodes
    # infected node infects susceptible node with probability 'alpha_raw' in one unit of time 
    # infected node becomes 'removed' node with probability 'beta_raw' in one unit of time
    alpha = alpha_raw*dt 
    beta = beta_raw*dt
    
    state=np.zeros(N)
    state[0]=1

    # 'active' queue manages infected nodes
    active = queue.queue()
    active.enqueue(0)

    # main loop
    timer = 0
    while not active.is_empty() and timer < time:
        # dequeue an infected node
        v = active.dequeue()
        # action on neighborhood(v)
        for w in adj[v]:
            if state[w] == 0:
                # neighbors of v may become active
                o = np.random.rand()
                if o < alpha:
                    state[w] = 1
                    active.enqueue(w)
        y = np.random.rand()
        if y < beta:
            state[v] = 2
        else:
            active.enqueue(v)

        timer += 1
        
    return state

if __name__ == '__main__':
    import time
    sims = 2

    t3 = time.time()
    for i in xrange(sims):
        simulation(N=80,graph='random')
    t4 = time.time()
    print t4 - t3

    