# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 15:48:10 2015

@author: Nickhil_Sethi
"""
#from graph_tool.all import *
import numpy as np
from network import *
import queue

'''
These are two functions that are used both in constructing random graphs, and running our
simulation.

'''

#Output: Performs vertex_transition on each v in the graph. Updates state

# what is more efficient?
# iteration through 'active' set
# or lookup in hash map


# this always iterates through N nodes
def dynamics(N,state,adj):
    for v in xrange(N):
        if state[v] == 1:
            for w in adj[v]:
                if state[w] == 0:
                    o = np.random.rand()
                    if o < alpha:
                        state[w] = 1
            y = np.random.rand()
            if y < beta:
                state[v] = 2
    return state

# this only iterates through 'active nodes'
def dynamics_2(N,state,active,adj,remove_stack):
    # iteration through active nodes is O(n)

    L = active.size
    counter = 0
    while not active.is_empty() and counter < L:
        counter += 1
        v = active.dequeue()
        # action on neighborhood is O(m)
        for w in adj[v]:
            # O(1)
            if state[w] == 0:
                o = np.random.rand()
                if o < alpha:
                    state[w] = 1
                    active.enqueue(w)        
        # removal of i from is O(n)
        y = np.random.rand()
        if y < beta:
            state[v] = 2
        else:
            active.enqueue(v)
    return state

def simulation_1(N=100,time=100,graph='random',delta=.5, w=.5,p=.5,dt=.01,alpha_raw=1.0,beta_raw=1.0):
    graphs = ['random','scale free','small world']

    if not graph in graphs:
        raise ValueError('graph must be type [random, scale free, small world]')

    global alpha, beta
    alpha = alpha_raw*dt 
    beta = beta_raw*dt
    state=np.zeros(N)
    state[0]=1

    if graph == 'random':
        adj = construct_random_graph(N,delta)
    elif graph == 'scale free':
        adj = construct_scale_free_graph(N,w)
    else:
        adj = construct_small_world_graph(N,p)

    for i in range(time):                      
        state=dynamics(N,state,adj)

    return state

def simulation_2(N=100,time=100,graph='random',delta=.5, w=.5,p=.5,dt=.01,alpha_raw=1.0,beta_raw=1.0):
    graphs = ['random','scale free','small world']

    if not graph in graphs:
        raise ValueError('graph must be type [random, scale free, small world]')

    global alpha, beta
    alpha = alpha_raw*dt 
    beta = beta_raw*dt
    
    state=np.zeros(N)
    state[0]=1

    if graph == 'random':
        adj = construct_random_graph(N, delta)
    elif graph == 'scale free':
        adj = construct_scale_free_graph(N,w)
    else:
        adj = construct_small_world_graph(N,p)

    active = queue.queue()
    active.enqueue(0)

    timer = 0
    while not active.is_empty() and timer < time:
        v = active.dequeue()
        for w in adj[v]:
            if state[w] == 0:
                o = np.random.rand()
                if 0 < alpha:
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

    sims = 2
    
    import time
    t1 = time.time()
    for i in xrange(sims):
        simulation_1(N=510,graph='random')
    t2 = time.time()
    print t2 - t1

    t3 = time.time()
    for i in xrange(sims):
        simulation_2(N=510,graph='random')
    t4 = time.time()
    print t4 - t3


    