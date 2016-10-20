'''

network module

@author: Nickhil-Sethi

'''

import queue
import stack
import binary_tree

import numpy.random
from copy import copy

def derange(arr):

    copy_array        = copy(arr)

    start_index       = 0
    end_index         = len(arr) - 1
    len_list          = len(arr)

    while len_list > 0:
        
        k                                       = numpy.random.randint(len_list)
        arr[start_index + k], arr[end_index]    = arr[end_index], arr[start_index + k]

        start_index                             += 1
        end_index                               -= 1

        len_list                                = end_index - start_index + 1

    for index in xrange(len(arr)//2):
        early   = arr[index]
        late    = arr[-(index + 1)]

        i1 = copy_array.index(early)
        i2 = copy_array.index(late) 

        copy_array[i1], copy_array[i2] = copy_array[i2], copy_array[i1]

    return copy_array

class Node(object):
    def __init__(self,index,value=None):
        self.value          = value 
        self.index          = index
        self.adjacency_set  = binary_tree.binary_search_tree()
        self.explored       = False
    
    def connect(self,target_index):
        self.adjacency_set.insert(target_index)
    
    def disconnect(self,target_index):
        self.adjacency_set.delete(target_index)

    def connects_to(self,target_index):
        return (target_index in self.adjacency_set)

class Network(object):
    def __init__(self):
        self.size   = 0
        self.nodes  = {}
    
    def __contains__(self,n):
        return (n in self.nodes)
    
    def add_node(self,index,value=None):
        if index in self:
            raise IndexError('nodes %d already in graph' % index)
        new_node = Node(index,value)
        self.nodes[index] = new_node
    
    def remove_node(self,index):
        if index in self:
            for n in self.nodes:
                if index in self.nodes[n]:
                    self.nodes[n].disconnect(index)
            return self.nodes.pop(index)

class GeneNetwork(Network):
    def __init__(self,p):
        Network.__init__(self)
        self.p      = p

    def construct(self, num_nodes, num_edges):

        for i in xrange(num_nodes):
            self.add_node(i)

        self_edges     = range(num_nodes)
        nonSelf_edges  = zip(range(num_nodes),derange(range(num_nodes)))

        numpy.random.shuffle(self_edge_stack)
        numpy.random.shuffle(non_self_edge_stack)

        edge_counter    = 0
        selected_edges  = []

        while edge_counter <= num_edges:
            o = numpy.random.rand()
            if o <= self.p and self_edge_stack:
                selected_edges.append( (len(self_edge_stack) - 1, self_edge_stack.pop() )  )
            else:
                selected_edges.append( non_self_edge_stack.pop() )
            edge_counter += 1

        for edge in selected_edges:
            self.nodes[edge[0]].connect(edge[1])

        return selected_edges


if __name__=='__main__':

    G = GeneNetwork(.3)
    G.construct(20,20)

