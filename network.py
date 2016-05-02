'''

network module.

nodes must be real valued

@author: Nickhil-Sethi

'''

import numpy as np
import binary_tree

class node(object):
    def __init__(self,value,index):
        self.value = value 
        self.index = index
        self.adj_tree = binary_tree.binary_search_tree()

class graph(object):
    def __init__(self,node_map={},directed=False,loops=False):
        
        # maps node indices to node values
        self.node_map = node_map

        # number of nodes
        self.N = len(self.node_map)

        # boolean true if graph is directed
        self.directed = directed

        # this way? or with node object?
        self.node = {}
        self.indices = []
        for n in self.node_map:
            self.indices.append(n)
            self.node[n] = node(value=self.node_map[n],index=n)

    # connect node i to node j
    def connect(self,i,j):
        if not i in self.node_map:
            raise IndexError(i ,' not in adjacency list')
        if not j in self.node_map:
            raise IndexError(j ,' not in adjacency list')

        # search first if this is in there
        if not self.node[i].adj_tree.binary_search( j ):
            self.node[i].adj_tree.insert( j )

        if not self.directed:
            if self.node[j].adj_tree.binary_search( i ) == None:
                self.node[j].adj_tree.insert( i )

    def disconnect(self,i,j):
        if i not in adj:
            raise IndexError('%i not in adjacency list',i)
        if j not in adj:
            raise IndexError('%j not in adjacency list',j)
        
        adj[i].remove(j)
        if self.directed:
            adj[j].remove(i)

class random_graph(graph):

    def __init__(self,nodes={},delta=.5,directed=False):
        graph.__init__(self,nodes,directed)
        self.delta = delta

    def construct(self):
        # faster iteration loop if graph is undirected
        if not self.directed:
            for i in xrange(self.N):
                for j in xrange(i+1,self.N):
                    if np.random.rand() < self.delta:
                        self.connect(self.indices[i],self.indices[j])
        # else 
        else:
            # for each node
            for i in self.nodes:
                # can be more space efficient?
                for j in self.nodes:
                    # nodes are not self connected
                    if loops:
                        if np.random.rand() < self.delta:
                            self.connect(i,j)
                    elif not loops and j != i:
                        # if random number ~U[0,1] < delta
                        if np.random.rand() < self.delta:
                            self.connect(i,j)
        
        adj_list = {}
        for n in self.node:
            adj_list[n] =  self.node[n].adj_tree.return_as_array()
        return adj_list

    def parallel_construct(self,threads=2):

        # T(N) = 2*T(N/2) + (n**2)/4

        # construct two graphs of size ~ N/2 
        # join two graphs by iterating

        # g1 and g2 must be randomly sampled 

        adj = g1_adj + g2_adj

        # return two networks to main thread 
        # and connect them via standard procedure
        for n in G1:
            for m in G2:
                o = np.random.rand()
                if o < delta:
                    connect(m,n,adj)

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
        adj[i] = binary_tree.binary_search_tree()
    
    connect(0,1,adj)

    for v in xrange(2,N):

        U = [ 1./float(v) for i in xrange(v) ]
        X = [ (1-w)*U[i] + (w)*(Pr[i]) for i in xrange(v)]
        
        x = np.random.choice(range(v), size = None , replace = True, p = X)
        connect(v,x,adj)

        l = [ len(adj[i].return_as_array()) for i in xrange(v+1) ]
        
        # update Preferential distribution
        total = sum(l)
        Pr = [float(l[i])/float(total) for i in xrange(v+1)]

    adj_list = [ adj[i].return_as_array() for i in xrange(N)]
    return adj_list
    
#Input: Number of vertices N, parameter p
#Constructs graph by beginning with circular ring on which every vertex is connected
#to the two nearest neighbors on each side. With probability p each edge is broken and
#reconnected to another vertex chosen from a uniform distribution
#Output: Adjacency matrix
def construct_small_world_graph(N, p):
    adj = {}
    for i in xrange(N):
        adj[i] = binary_tree.binary_search_tree(binary_tree.binary_node(i))

    for i in xrange(N):
        connect(i, (i-1)%N, adj)
        connect(i, (i+1)%N, adj)
        connect(i, (i-2)%N, adj)
        connect(i, (i+2)%N, adj)
    
    nodes = set(range(N))
    for i in range(N):
        for j in range(i+1,N):
            if j in adj[i].return_as_array():
                o = np.random.rand()
                if(o < p):
                    nodes.remove(j)
                    x = np.random.choice(list(nodes))
                    nodes.add(j)
                    disconnect(i,j,adj)
                    connect(i,x,adj)

    return adj


#Input: An array state of the states
if __name__=='__main__':
    import time

    N = 800

    node_map = {}

    for i in xrange(N):
        node_map[2*i] = np.random.randint(40)

    t3 = time.time()
    G = random_graph(node_map,delta=.3)
    t4 = time.time()
    print t4-t3
    t1 = time.time()
    adj=G.construct()
    t2 = time.time()
    print t2-t1
    