import linked_list
class hash_map(object):
	def __init__(self,size):
		self.size = size
		self.items = [linked_list.linked_list()]*self.size

	def hash_function(self,item):
		if not isinstance(item,__builtins__.int):
			raise TypeError('maps type(int) only')
		return item%self.size
	def put(self,key,value):
		index = self.hash_function(key)
		self.items[index].insert([key,value])
	def get(self,key):
		index = self.hash_function(key)

		if self.items[index].is_empty():
			return 
		found = False
		while not found:
			if 
	def __getitem__(self,key):
		return self.get(key)
	def __setitem__(self,key,value):
		self.put(key,value)
		return
if __name__=='__main__':
	h = hash_map(5)
	h[0] = 1
	print h[0]
	