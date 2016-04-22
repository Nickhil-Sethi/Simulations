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
    

def dynamics(N,state, adj):
    state_new = [vertex_transition(v,adj,state) for v in xrange(N)]
    return state_new

def simulation(N=100,time=100,graph='random',delta=.5,w=.5,p=.5,dt=.01,alpha_raw=1.0,beta_raw=1.0):

    if graph == 'random':
        adj = construct_random_graph(N,delta)
    elif graph == 'scale free':
        adj = construct_scale_free_graph(N,w)
    else:
        adj = construct_small_world_graph(N,p)
    

    global alpha,beta 
    alpha = alpha_raw*dt 
    beta = beta_raw*dt

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
            

        state=dynamics(N,state,adj)
        print state  

    return 
def main(N=100,graph='random'):
    
    graphs = ['random','scale free','small world']
    if not graph in graphs:
        raise TypeError('graph must be either random, scale free, or small world')

    thing = np.zeros((3,num_simulations))
    for ii in range(num_simulations):
        
        if graph == 'random':
            adj = construct_random_graph(N,delta)
        elif graph == 'scale free':
            adj = construct_scale_free_graph(N,w)
        else:
            adj = construct_small_world_graph(N, p)
        
        state = np.zeros(N)
        
        state[0] = 1
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
            
            plots[:,i] = [counter_s , counter_i , counter_r]
            dynamics(state,adj)  
            for k in range(N):
                cost = cost + plots[1,k]*dt
            
        fs = plots[0, time-1]
        fi = plots[1, time-1]
        fr = plots[2, time-1]
        #print fs , fi , fr
        thing[0,ii] = fs
        thing[1, ii] = fi
        thing[2, ii] = fr
        
        if(plots[0 , time - 1] < 20):
            nepidemic = nepidemic + 1
        #print cost  
        #plot(plots[0,:])
        #plot(plots[1,:])
        #plot(plots[2,:])
        #show()
        avg_cost = avg_cost + (float(1)/float(num_simulations))*cost
        avg = avg + (float(1)/float(num_simulations))*plots
        connect = connect + (float(1)/float(num_simulations))*average_centrality(adj)
        
    if(q==0):
        print 'Random'
        print "delta = ", delta
    if(q == 1):
        print 'Scale Free'
        print "omega = ", w
    if(q == 2):
        print 'Small World'
        print "p = ", p
        
    print "Number of Simulations = ", num_simulations 
    print "N =", N
    print "dt =", dt 
    print "alpha = ", alpha_raw
    print "beta = ", beta_raw
    print "Number of Non-epidemics", nepidemic   
    print "Final S =", avg[0, time-1]
    print "Final I =", avg[1, time-1]
    print "Final R =", avg[2, time-1]
    print "Average Cost = ", avg_cost
    print "Average Connectivity =", connect
    plot(avg[0,:])
    plot(avg[1,:])
    plot(avg[2,:])

    #figure(2)
    #hist(thing[0,:])

    #figure(3)
    #hist(thing[1,:])

    #figure(4)
    #hist(thing[2,:])

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
    