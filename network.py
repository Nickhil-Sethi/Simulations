from collections import OrderedDict, deque
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
        self.color         = 'Black'

    def __repr__(self):
        return "Node {}".format(self.index)

    def connect(self,newNode,weight=None):
        self.adjacency_set.insert(newNode.index,(newNode,weight))

class DirectedGraph(object):
    def __init__(self,init_size):
        self.nodes         = [Node(i) for i in xrange(init_size)]

    def connect(self,i,j):
        self.nodes[i].connect(self.nodes[j])

    def BFS(self,s):
        queue = deque([self.nodes[s]])
        while queue:
            current = queue.pop()
            if current.color == 'Black':
                print "recoloring {}".format(current)
                current.color = 'Red'
                for node in current.adjacency_set:
                    queue.appendleft(node[0])


if __name__=='__main__':
    G = DirectedGraph(10)
    print G.nodes

    G.connect(2,4)
    G.connect(0,5)
    G.connect(0,2)
    G.connect(4,8)
    G.connect(8,9)

    G.BFS(0)
    a = G.nodes[0]
    for i in a.adjacency_set:
        print i