# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 15:48:10 2015

@author: Nickhil_Sethi
"""
#from graph_tool.all import *
import numpy as np
#import matplotlib.pyplot as plt
#close('all')
#s = 0 


'''
These are two functions that are used both in constructing random graphs, and running our
simulation.

'''


def connect(i,j,adj,symmetric=True):
    if not i in adj:
        raise IndexError('i not in adjacency list')
    if not j in adj:
        raise IndexError('j not in adjacency list')
    
    adj[i].add(j)
    if symmetric:
        adj[j].add(i)

def disconnect(i,j,adj,symmetric=True):
    if i not in adj:
        raise IndexError('i not in adjacency list')
    if j not in adj:
        raise IndexError('j not in adjacency list')
    
    adj[i].remove(j)
    if symmetric:
        adj[j].remove(i)

def construct_random_graph(N, delta):

    adj_list = {}
    nodes = range(N)

    for i in nodes:
        adj_list[i] = set()
    # for each node
    others = set(nodes)
    for i in nodes:
        # can be more space efficient?
        others.remove(i)
        for j in list(nodes):
            # if random number ~U[0,1] < delta
            if np.random.rand() < delta:
                connect(i,j,adj_list)
        others.add(i)

    return adj_list

#Constructs scale free graph
#Input: number of vertices, parameter omega
#Adds vertices sequentially, connects to vertex i with proability w*U(i) + (1-w)*Pr(i)
#U is uniform distribution, Pr(i) = d(i)/sum_j (d_j), where d(i) represents the number of edges
#vertex i has
#Output: Adjacency matrix    
def construct_scale_free_graph(N, w):
    
    Pr = []
    Pr.append(.5)
    Pr.append(.5)

    adj = {}
    for i in xrange(N):
        adj[i] = set()
    
    adj[0].add(1)
    adj[1].add(0)

    for v in xrange(2,N):

        U = [ 1./float(v) for i in xrange(v) ]
        X = [ (1-w)*U[i] + (w)*(Pr[i]) for i in xrange(v)]
        
        x = np.random.choice(range(v), size = None , replace = True, p = X)
        connect(v,x,adj)

        l = [ len(adj[i]) for i in xrange(v+1) ]
        
        # update Preferential distribution
        total = sum(l)
        Pr = [float(l[i])/float(total) for i in xrange(v+1)]

    return adj
    
#Input: Number of vertices N, parameter p
#Constructs graph by beginning with circular ring on which every vertex is connected
#to the two nearest neighbors on each side. With probability p each edge is broken and
#reconnected to another vertex chosen from a uniform distribution
#Output: Adjacency matrix
def construct_small_world_graph(N, p):
    adj = {}
    for i in xrange(N):
        adj[i] = set()

    for i in xrange(N):
        connect(i, (i-1)%N, adj)
        connect(i, (i+1)%N, adj)
        connect(i, (i-2)%N, adj)
        connect(i, (i+2)%N, adj)
    
    nodes = set(range(N))
    for i in range(N):
        for j in range(i+1,N):
            if j in adj[i]:
                o = np.random.rand()
                if(o < p):
                    nodes.remove(j)
                    x = np.random.choice(list(nodes))
                    nodes.add(j)
                    disconnect(i,j,adj)
                    connect(i,x,adj)

    return adj


#Input: A fixed vertex v, in_V the in-neighborhood of V, 
#state the array representing the states (S, I ,R) of each vertex

#Output: Updates state based on neighborhood of v. If v succeptible, draws bernoulli random
#variable with success probability alpha*dt for every infected agent in its neighborhood
#if infected, v becomes removed with probability beta*dt

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
    

#Input: An (N x N) adjacency matrix

#Output: A list "all_neighborhoods" of arrays, with all_neighborhoods[v] representing
#the neighborhood of vertex v

def average_centrality(adj):  
    N = len(adj)
    l = np.zeros(N)
    neighborhoods = find_all_in_neighborhoods(adj)
    for i in range(N):
        l[i] = len(neighborhoods[i])
        
    total = sum(l)
    avg = float(total)/float(N)
    
    return avg

#Input: An array state of the states of each vertex. The adjacency matrix of the network.

#Output: Performs vertex_transition on each v in the graph. Updates state

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
    