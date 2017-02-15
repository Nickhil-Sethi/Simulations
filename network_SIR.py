# -*- coding: utf-8 -*-
"""
@author: Nickhil_Sethi

SIR simulation on network
"""

import queue
import numpy as np

from network import *

def simulation(N=100,time=100,graph='random',delta=.1, w=.5,p=.5,dt=.01,alpha_raw=1.0,beta_raw=1.0):

    assert graph in ['random','scale free','small world']
    assert 0. <= delta <= 1.
    assert 0. <= w <= 1.
    assert 0. <= p <= 1.

    alpha    = alpha_raw*dt 
    beta     = beta_raw*dt
    state    = [0 for i in xrange(N)]
    state[0] = 1

    print "     constructing graph..."
    if graph == 'random':
        G = random_graph(node_map=state,delta=delta)
        adj = G.construct()
    elif graph == 'scale free':
        adj = construct_scale_free_graph(N,w)
    else:
        adj = construct_small_world_graph(N,p)

    # state transition probabilities for nodes
    # infected node infects susceptible node with probability 'alpha_raw' in one unit of time 
    # infected node becomes 'removed' node with probability 'beta_raw' in one unit of time

    print "     simulating disease spread"
    # 'active' queue manages infected nodes
    active = queue.queue()
    active.enqueue(0)

    # main loop; essentially a BFS
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
    sims = 1

    t3 = time.time()
    for i in xrange(sims):
        st= simulation(N=1000,graph='random')
        print st
    t4 = time.time()
    print t4 - t3

    