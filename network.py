'''

network module. nodes must be real valued

@author: Nickhil-Sethi

'''

import threading
import queue
import stack
import numpy as np
import binary_tree

class node(object):
    def __init__(self,value,index=None):
        self.value = value 
        self.index = index
        self.adj_tree = binary_tree.binary_search_tree()
        self.explored = False

class graph(object):
    def __init__(self,node_map=[],directed=False,loops=False):
        
        # sanity check
        if not type(node_map) is list:
            raise TypeError('node map must be type list')

        # list of node values 
        self.node_map = node_map
        
        # number of nodes
        self.N = len(node_map)

        # boolean true if graph is directed
        self.directed = directed

        # node dictionary
        self.node = {}

    def connected(self,i,j):
        if not 0 <= i < self.N:
            raise IndexError(' not in adjacency list')
        if not 0 <= j < self.N:
            raise IndexError(' not in adjacency list')

        # search first if this is in there
        if not self.node[i].adj_tree.binary_search(j):
            return False
        else:
            return True
            
    # connect node i to node j
    def connect(self,i,j):

        # search first if this is in there
        if not self.node[i].adj_tree.binary_search(j):
            self.node[i].adj_tree.insert( j )

        if not self.directed:
            if self.node[j].adj_tree.binary_search( i ) == None:
                self.node[j].adj_tree.insert( i )

    def DFS(self,v,search_value):
        if self.node[v].value == search_value:
            return v

        self.node[v].explored = True
        s = stack.stack()
        s.push(v)


        while not s.is_empty():
            u = s.pop()
            if self.node[u].value == search_value:
                return u
            else:
                for w in self.adj_list[u]:
                    if not self.node[w].explored:
                        self.node[w].explored = True
                        s.push(w)

        return None

    def BFS(self,v,search_value):
        if self.node[v].value == search_value:
            return v

        self.node[v].explored = True
        q = queue.queue()
        q.enqueue(v)

        while not q.is_empty():
            u = q.dequeue()
            if self.node[u].value == search_value:
                return u
            else:
                for w in self.adj_list[u]:
                    if not self.node[w].explored:
                        self.node[w].explored = True
                        q.enqueue(w)

        return None

    def connected_component(self,v):

        BFS_tree = [ [] for i in xrange(self.N) ]

        i = 0
        L = [ queue.queue() ]
        L[0].enqueue(v)

        self.node[v].explored = True
        

        while not L[i].is_empty():

            # initialize next layer
            L.append( queue.queue() )
            
            # choose node from i'th layer
            u = L[i].dequeue()
            for w in self.adj_list[u]:
                if not self.node[w].explored:
                    self.node[w].explored = True

                    BFS_tree[u].append(w)
                    L[i+1].enqueue(w)

            i+=1

        return BFS_tree

class random_graph(graph):

    def __init__(self,node_map=[],delta=.5,directed=False):
        graph.__init__(self,node_map,directed)
        self.delta = delta

    def construct(self):
        for i,n in enumerate(self.node_map):
            self.node[i] = node(value=n,index=i)
        
        # faster iteration loop if graph is undirected
        if not self.directed:
            for i in xrange(self.N):
                for j in xrange(i+1,self.N):
                    if np.random.rand() < self.delta:
                        self.node[i].adj_tree.insert(j)
                        self.node[j].adj_tree.insert(i)
        # else 
        else:
            # for each node
            for i in self.N:
                # can be more space efficient?
                for j in self.N:
                    # nodes are not self connected
                    if loops:
                        if np.random.rand() < self.delta:
                            self.node[i].adj_tree.insert(j)
                    elif not loops and j != i:
                        # if random number ~U[0,1] < delta
                        if np.random.rand() < self.delta:
                            self.node[i].adj_tree.insert(j)       
        
        self.adj_list = [ self.node[n].adj_tree.in_order() for n in xrange(self.N)] 
        return self.adj_list

    # useful for constructing larger graphs
    # N ~ 1000
    def parallel_construct(self):
        return
     
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
        adj[i] = binary_tree.binary_search_tree(binary_tree.binary_node())

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

    N = 100
    trials = 1

    node_map = [np.random.randint(10) for i in xrange(N)]

    t1 = time.time()
    for i in xrange(trials):
        G=random_graph(node_map=node_map,delta=.2)
        G.construct()
        print G.connected_component(0)
    t2 = time.time()

    print (t2-t1)/float(trials)
