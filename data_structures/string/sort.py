import heapq

def is_sorted(arr):
	for i in xrange( len(arr) - 1 ):
		if arr[i] > arr[i+1]:
			return False
	return True

def bubble_sort(arr):
	swap = True
	while swap:
		swap = False
		for i in xrange(len(arr)-1):
			if arr[i] > arr[i+1]:
				temp = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = temp
				swap = True
	return arr

def selection_sort(arr):
	for i in xrange(len(arr),0,-1):
		m = arr[0]
		for j in xrange(i):
			if arr[j] > m:
				m     = arr[j]
				arg_m = j 
		temp 		= arr[i-1]
		arr[i-1] 	= m
		arr[arg_m] 	= temp

	return arr

def insertion_sort(arr):

	for i in xrange(1,len(arr)):
		pos           = i
		current_value = arr[i]
		while pos > 0 and arr[pos-1] > current_value:
			arr[pos] = arr[pos-1]
			pos      -=1
		arr[pos] = current_value
	return arr

def gap_insertion_sort(arr,position,sublist_count):

	for i in xrange(position,len(arr)):
		p     = i
		c_val = arr[i]
		while p > position and arr[p - sublist_count] > c_val:
			arr[p] = arr[p - sublist_count]
			p      -= sublist_count
		arr[p] = c_val

	return arr

def shell_sort(arr):
	k = 2
	sublist_count = len(arr)//k
	while sublist_count > 0:
		for position in xrange(sublist_count):
			gap_insertion_sort(arr,position,sublist_count)
		k+=1
		sublist_count = len(arr)//k
	return arr

def merge(arr,start,pivot,end):

	new_arr = []

	c1 = start
	c2 = pivot
	while c1 < pivot and c2 <= end:

		if arr[c1] < arr[c2]:
			new_arr.append( arr[c1] )
			c1 += 1
		else:
			new_arr.append( arr[c2] )
			c2 += 1
	
	while c1 < pivot:
		new_arr.append( arr[c1] )
		c1 += 1
	while c2 <= end:
		new_arr.append( arr[c2] )
		c2 += 1
	
	for i in xrange(start,end):
		arr[i] = new_arr[i - start]
	return arr

def merge_sort(arr,start=None,end=None):

	# default parameters 
	if not start:
		start = 0
	if not end:
		end = len(arr)-1

	# base case; length 2 array
	if (end - start) == 1:
		
		if arr[start] > arr[end]:
			temp = arr[end]
			arr[end] = arr[start]
			arr[start] = temp

		return arr

	pivot = (end + start)//2

	merge_sort(arr, start, pivot)
	merge_sort(arr, pivot , end)
	merge(arr, start, pivot, end)
	
	return arr


def heapSort(arr):
	ret  = []
	heapq.heapify(arr)
	while arr:
		ret.append(heapq.heappop(arr))
	return ret 

def Merge(lists):
	values = []
	for _list in lists:
		values = values + _list

	heapq.heapify(values)
	
	ret = []
	while values:
		ret.append(heapq.heappop(values))
	return ret

def MergeRecursive(lists):
	if len(lists) == 2:
		lists[0] = heapSort(lists[0])
		lists[1] = heapSort(lists[1])
		return Merge(lists)
	if len(lists) == 1:
		return heapSort(lists[0])
	if len(lists) == 0:
		return

	n     = len(lists)//2
	list1 = [lists[i] for i in xrange(n)]
	list2 = [lists[j] for j in xrange(n,len(lists))]
	L     = MergeRecursive(list1)
	R     = MergeRecursive(list2)

	return Merge([L,R])

def partition(arr,left,right):
	partition 		 			  = arr[(left+right)//2]
	while left <= right:
		while arr[left] < partition:
			left				 +=1
		while arr[right] > partition:
			right				 -=1
			
		if left <= right:
			arr[right], arr[left] = arr[left], arr[right]
			left				 +=1
			right				 -=1
	return left

def quickSort(arr,left,right):
	if left < right:
		p 	= partition(arr,left,right)
		arr = quickSort(arr,left,p-1)
		arr = quickSort(arr,p,right)
	return arr

if __name__=='__main__':

	import numpy as np

	L = 10
	S = 14
	for i in xrange(1000):
		A = [np.random.randint(L) for i in xrange(S)]
		A = quickSort(A,0,S-1)
		if not is_sorted(A):
			raise Exception('NOT SORTED')