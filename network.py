import numpy as np
import binary_tree

def connect(i,j,adj,symmetric=True):
    if not i in adj:
        raise IndexError('i not in adjacency list')
    if not j in adj:
        raise IndexError('j not in adjacency list')
    
    adj[i].add(j)
    if symmetric:
        adj[j].insert(i)

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
        adj_list[i] = binary_tree.binary_tree()
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

#Input: An array state of the states