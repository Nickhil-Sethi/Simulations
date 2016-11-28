import numpy as np

def linear_search(mylist,item):
	for index, element in enumerate(mylist):
		if element == item:
			return index
	return -1

def binary_search(mylist,item):

	begin=0.
	end=float(len(mylist)-1)
	mid = int(np.ceil((begin+end)/2))

	keep_going = True
	while keep_going:

		if end - mid < 1:
			keep_going = False

		if mylist[mid] == item:
			return mid
		elif mylist[mid] < item:
			begin = mid
			mid = int(np.ceil((begin+end)/2))
		else:
			end = mid
			mid = int(np.ceil((begin+end)/2))
	
	return -1

if __name__ == '__main__':
	my_list = range(4324)
	print linear_search(my_list,-3)
	print binary_search(my_list,-3)