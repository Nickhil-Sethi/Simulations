# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 15:48:10 2015

@author: Nickhil_Sethi
"""
#from graph_tool.all import *
import numpy as np
import matplotlib.pyplot as plt
#close('all')
#s = 0 


'''
These are two functions that are used both in constructing random graphs, and running our
simulation.

'''

#Input: A fixed vertex v, adjacency matrix adj

#Output: Provides array representing "in-neighborhood" of v 
#(i.e. vertices which connect to v. If adj is symmetric, in-neighborhood 
#and out-neighborhood are the same) 

def find_in_neighborhood(v,adj):
    neighborhood_v = []
    for j in range(N):
        if(adj[j][v] == 1):
            neighborhood_v.append(j)
    return neighborhood_v


#Input: A number and a set containing that number.
#Output a randomly chosen number that is not the input number, from uniform distribution

#Input: a number of vertices, parameter delta
#Constructs graph as follows: N vertices, sets i <=> j with probability delta
#Output: Adjacency matrix

def construct_random_graph(N, delta):

    adj_list = {}
    nodes = range(N)

    # for each node
    for i in nodes:
        adj_list[i] = set()

        # can be more space efficient?
        others = list(set(nodes).remove(i))
        for j in others:

            # if random number ~U[0,1] < delta
            if np.random.rand() < delta:
                adj_list[i].add(j)

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
    adj = np.zeros((N,N))
    adj[0,1] = 1
    adj[1,0] = 1
    for v in range(2,N):
        #print len(range(v))
        #print len(Pr)
        U = []
        for i in range(v):
            U.append(float(1)/float(v))
        X = []
        for i in range(v):
            X.append( (1-w)*U[i] + (w)*(Pr[i]) )
        x = np.random.choice(range(v), size = None , replace = True, p = X)
        adj[v,x] = 1
        adj[x,v] = 1
        l = []
        for i in range(v+1):
            l.append(len(find_in_neighborhood(i,adj)))
        total = sum(l)
        Pr = []
        for i in range(v+1):
            Pr.append(float(l[i])/float(total))
    

    return adj
    
#Input: Number of vertices N, parameter p
#Constructs graph by beginning with circular ring on which every vertex is connected
#to the two nearest neighbors on each side. With probability p each edge is broken and
#reconnected to another vertex chosen from a uniform distribution
#Output: Adjacency matrix
def construct_small_world_graph(N, p):
    adj = np.zeros((N,N))
    for i in range(2,N-2):
        adj[i,i-1] = 1
        adj[i-1,i] = 1
        
        adj[i,i+1] = 1
        adj[i+1,i] = 1
        
        adj[i,i-2] = 1
        adj[i-2,i] = 1
        
        adj[i+2,i] = 1
        adj[i,i+2] = 1
    
    if(i == 0):
        adj[0,1] = 1
        adj[1,0] = 1
        adj[0,2] = 1
        adj[2,0] = 1
        adj[0,N-1] = 1
        adj[N-1,0] = 1
        adj[0,N-2] = 1
        adj[N-2,0] = 1
    if(i == 1):
        adj[0,1] = 1
        adj[1,0] = 1
        adj[0,2] = 1
        adj[2,0] = 1
        adj[0,N-1] = 1
        adj[N-1,0] = 1
        adj[0,N-2] = 1
        adj[N-2,0] = 1
    for i in range(N):
        for j in range(N):
            if(adj[i,j] == 1):
                o = uniform(0,1)
                if(o < p):
                    adj[i,j] = 0
                    adj[j,i] = 0
                    x = choose_random(i,N)
                    adj[i,x] = 1
                    adj[x,i] = 1
    
    k = 2
    
    return adj , k


#Input: A fixed vertex v, in_V the in-neighborhood of V, 
#state the array representing the states (S, I ,R) of each vertex

#Output: Updates state based on neighborhood of v. If v succeptible, draws bernoulli random
#variable with success probability alpha*dt for every infected agent in its neighborhood
#if infected, v becomes removed with probability beta*dt

def vertex_transition(v, in_V, state):
    if(state[v] == 0):
        for x in in_V:
            if(state[x] == 1):
                o = uniform(0,1)
                #print o
                if(o < alpha):
                    state[v] = 1
                    #print("yes")
    if(state[v] == 1):
        o = uniform(0,1)
        if(o < beta):
            state[v] = 2 
    return state[v]
    

#Input: An (N x N) adjacency matrix

#Output: A list "all_neighborhoods" of arrays, with all_neighborhoods[v] representing
#the neighborhood of vertex v

def find_all_in_neighborhoods(adj):
    all_neighborhoods = []
    for v in range(N):
        in_v = find_in_neighborhood(v,adj)
        all_neighborhoods.append(in_v)
        
    return all_neighborhoods

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

def dynamics(state, adj, in_neighborhoods):  
    state_new = np.zeros(N)
    for v in range(N) :
        in_v = in_neighborhoods[v]
        state_new[v] = vertex_transition(v, in_v, state) 
        
    state = state_new
    return state,adj

def main():
    thing = np.zeros((3,num_simulations))
    for ii in range(num_simulations):
        
        adj, q = construct_random_graph(N,delta)
        #adj , q = construct_scale_free_graph(N,w)
        #adj , q = construct_small_world_graph(N, p)

        in_neighborhoods = find_all_in_neighborhoods(adj)
        
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
            dynamics(state,adj,in_neighborhoods)  
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

    #random graph parameter
    delta = .037
    #scale free graph parameter
    w = 0.0
    #small-world parameter
    p = .6

    num_simulations = 1
    dt = .01
    time = 1000
    sick = np.zeros(time)
    N = 100 
    state = np.zeros(N)
    adj = np.zeros((N,N))
    alpha_raw = 1.0
    beta_raw = 1.0
    alpha = alpha_raw*dt
    beta = beta_raw*dt
    plots = np.zeros((3,time))
    avg = np.zeros((3,time))
    avg_cost = 0
    connect = 0
    nepidemic = 0

    state[0] = 1

    print construct_random_graph(20, .5)
    #Main Program. Simulates num_simulation disease spreads, with newly generated graph
    #Every time.
    