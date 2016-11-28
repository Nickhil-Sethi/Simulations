def is_sorted(arr):

	for i in xrange( len(arr) - 1 ):
		if arr[i] > arr[i+1]:
			return False
	return True

def bubble_sort(arr):

	# early stopping condition
	swap = True
	while swap:
		swap = False
		for i in xrange(len(arr)-1):

			if arr[i] > arr[i+1]:
				# swap elements i and i+1
				temp = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = temp

				# keep going for one more loop at least
				swap = True

	return arr

def selection_sort(arr):

	for i in xrange(len(arr),0,-1):
		m = arr[0]
		for j in xrange(i):
			if arr[j] > m:
				m = arr[j]
				arg_m = j 
		temp = arr[i-1]
		arr[i-1] = m
		arr[arg_m] = arr[i-1]

	return arr

def insertion_sort(arr):

	for i in xrange(1,len(arr)):

		# starting position is current index
		pos = i
		current_value = arr[i]

		# shift array elements one by one until 
		# elements are less than current value
		while pos > 0 and arr[pos-1] > current_value:
			arr[pos] = arr[pos-1]
			pos-=1

		arr[pos] = current_value
	return arr

def gap_insertion_sort(arr,position,sublist_count):

	for i in xrange(position,len(arr)):

		p = i
		c_val = arr[i]

		while p > position and arr[p - sublist_count] > c_val:
			arr[p] = arr[p - sublist_count]
			p -= sublist_count

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

def partition(arr, pivot, low, high):

	# halt when low and high marker meet
	while low < high: 
		
		while arr[low] <= arr[pivot] and low < high and low < len(arr) - 1:
			low += 1

		while arr[high] >= arr[pivot] and high > low and high > 1:
			high -= 1

		if high > low:
			# swap low value with high value
			temp = arr[high]
			arr[high] = arr[low]
			arr[low] = temp

	# switch pivot value with high value
	temp = arr[high]
	arr[high] = arr[pivot]
	arr[pivot] = temp

	return high

def quicksort(arr, pivot, low, high):

	if low < high:
		
		p = partition(arr, pivot, low, high)
		print arr
		quicksort(arr, pivot, low, p-1)
		quicksort(arr, p, p+1, high)
	
	return arr

if __name__=='__main__':

	import numpy as np

	L = 10
	A = [np.random.randint(L) for i in xrange(L)]

	A = quicksort(A,0,1,9)
	print A
	