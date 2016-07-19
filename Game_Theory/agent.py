import sys
sys.path.insert(0,'/Users/Nickhil_Sethi/Code/Simulations')

import binary_tree as btree

class agent(binary_node):

	def __init__(self,index,strategy):

		self.key = index
		self.value = strategy

		self.left = None
		self.right = None
		self.parent = None

	def insert(self,agent):
		binary_node.insert(self,agent)

	def search(self,agentIndex):
		return binary_node.search(self,agentIndex)

	def deleteAgent(self,agent):
		binary_node.deleteNode(self,agent)