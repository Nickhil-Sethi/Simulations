# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 15:48:10 2015

@author: Nickhil_Sethi
"""
#from graph_tool.all import *
import numpy as np
from network import *
#import matplotlib.pyplot as plt
#close('all')
#s = 0 


'''
These are two functions that are used both in constructing random graphs, and running our
simulation.

'''

#Output: Performs vertex_transition on each v in the graph. Updates state

def vertex_transition(v, adj, state):
    if(state[v] == 0):
        for x in adj[v]:
            if(state[x] == 1):
                o = np.random.rand()
                #print o
                if(o < alpha):
                    state[v] = 1
                    #print("yes")
    if(state[v] == 1):
        o = np.random.rand()
        if(o < beta):
            state[v] = 2 
    return state[v]
    
# what is more efficient?
# iteration through 'active' set
# or lookup in hash map


# this always iterates through N nodes
def dynamics():
    for v in xrange(N):
        if state[v] == 1:
            for w in adj[v]:
                if state[v] == 0:
                    o = np.random.rand()
                    if o < alpha:
                        state[w] = 1
            y = np.random.rand()
            if y < beta:
                state[v] = 2

# this only iterates through 'active nodes'
def dynamics_2():
    # iteration through active nodes is O(n)
    for i in active:
        # action on neighborhood is O(m)
        for w in adj[i]:
            # O(1)
            if state[w] == 0:
                o = np.random.rand()
                if o < alpha:
                    state[w] = 1
                    active.add(w)
        # removal is O(n)
        y = np.random.rand()
        if y < beta:
            state[i] = 2
            active.remove(i)



def simulation(N=100,time=100,graph='random',delta=.5, w=.5,p=.5,dt=.01,alpha_raw=1.0,beta_raw=1.0):

    if graph == 'random':
        adj = construct_random_graph(N,delta)
    elif graph == 'scale free':
        adj = construct_scale_free_graph(N,w)
    else:
        adj = construct_small_world_graph(N,p)
    

    global N, alpha, beta, active, state
    alpha = alpha_raw*dt 
    beta = beta_raw*dt
    active = set()
    state=np.zeros(N)
    state[0]=1
    
    cost = 0   
    for i in range(time):          
        
        counter_i = 0
        counter_s = 0
        counter_r = 0
        for j in state:
            if(j == 0):
                counter_s = counter_s + 1  
            if(j == 1):
                counter_i = counter_i + 1           
            if(j == 2):
                counter_r = counter_r + 1  
                #print counter_s , counter_i , counter_r
            

        state = dynamics(N,state,adj)
        print state  

    return

if __name__ == '__main__':

        #i = 1
    #r = 2
    '''
    #random graph parameter
    delta = .037
    #scale free graph parameter
    w = 0.0
    #small-world parameter
    p=.6
    plots = np.zeros((3,time))
    avg = np.zeros((3,time))
    avg_cost = 0
    a_connect = 0
    nepidemic = 0
    '''
    simulation(N=20,graph='scale free',w=.1)
    #Main Program. Simulates num_simulation disease spreads, with newly generated graph
    #Every time.
    