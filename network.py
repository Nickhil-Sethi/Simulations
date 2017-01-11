import heapq
import numpy as np

from collections import OrderedDict, deque

from tree.heap import MinHeap
from tree.binary_tree import AVLTree

class AdjacencySet(AVLTree):
    def __init__(self):
        AVLTree.__init__(self)

    def inOrder(self):
        return [element.value for element in AVLTree.inOrder(self)]

    def __iter__(self):
        items = self.inOrder()
        for i,item in enumerate(items):
            yield item

class Node(object):
    def __init__(self,index,value=None):
        self.index         = index
        self.value         = value
        self.adjacency_set = AdjacencySet()
        self.explored      = False

    def connect(self,newNode,weight=None):
        self.adjacency_set.insert(newNode.index,(newNode,weight))

    def weight(self,index):
        s = self.adjacency_set.search(index)
        if s:
            return s.value[1]
        return None

    def __repr__(self):
        return "graph node {}".format(self.index)

class DirectedGraph(object):
    def __init__(self,init_size):
        self.nodes         = OrderedDict([(i,Node(i)) for i in xrange(init_size)])

    def connect(self,i,j,weight=None):
        self.nodes[i].connect(self.nodes[j],weight)

    def weight(self,i,j):
        return self.nodes[i].weight(j)

    def Dijsktras(self,s):
        S           = OrderedDict([(s,(0.,None))])
        done        = False
        while not done:
            done    = True
            dist    = np.inf
            prev    = None
            closest = None
            for i, (d,_) in S.items():
                for o, w in self.nodes[i].adjacency_set:
                    if o.index in S:
                        continue
                    if d+w < dist:
                        dist    = d+w
                        prev    = i
                        closest = o.index
            if closest:
                done       = False
                S[closest] = (dist,prev)
        return S

    def Dijksras_efficient(self,s):
        pq   = [s]
        dist = {q : self.weight(s,q) for q in self.nodes if q in self.nodes[s].adjacency_set else np.inf}
        while pq:
            u = pq.heappop()
            for v in self.nodes[u].adjacency_set:
                if dist[v] > dist[u] + self.weight(u,v):
                    dist[v] = dist[u] + self.weight(u,v)
                heapq.heappush(pq,v)

if __name__=='__main__':
    G = DirectedGraph(100)
    for n in G.nodes:
        for m in G.nodes:
            if m != n:
                G.connect(n,m,np.random.rand())
    print G.Dijsktras(2)