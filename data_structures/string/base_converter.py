import queue

def base_converter(num,base):
	if not isinstance(num,__builtins__.int):
		raise TypeError('must input type int')
	if not (2 <= base <= 16):
		raise ValueError('base must be between 2 and 16, inclusive')
	
	chars = '0123456789ABCDEFG'
	if num < base:
		return chars[num]
	else:
		r = chars[num%base]
		d = num//base
		return str(base_converter(d,base)) + r

def check_palindrome(string):
	if not isinstance(string,__builtins__.str):
		raise TypeError('must input type string')

	L = len(string)
	if L == 1:
		return True
	if L == 2:
		if string[0] == string[1]:
			return True
		else:
			return False
	else:
		return check_palindrome(string[1:L-1])

def recursive_sum(nums):

	L = len(nums)
	if L==1:
		return nums[0]
	else:
		return nums[0] + recursive_sum(nums[1:L])

def how_many_digits(num):
	if num < 10:
		return 1
	else:
		return how_many_digits(num//10) + 1

def recursive_max(num_list):
	l = len(num_list)
	if l == 1:
		return num_list[0]
	else:
		return max(num_list[0],recursive_max(num_list[1:l]))

def flatten_list(input):
	q       = queue.queue()
	counter = 0
	while counter < len(input):
		if not isinstance(input[counter],__builtins__.list):
			q.enqueue(input[counter])
		else:
			sub_list=flatten_list(input[counter])
			for i in sub_list:
				q.enqueue(i)
		counter +=1 
	
	new_list = []
	while not q.is_empty():
		new_list.append(q.dequeue())

	return new_list


if __name__ == '__main__':
	print base_converter(32,4)
	print check_palindrome('abacaba')
	print recursive_sum([0,1,2,3,4,5])
	print how_many_digits(3)
	print recursive_max([2,4,6,2,4,5,2,4,6,7,8,9])
	print flatten_list([1,2,[1,[2,1,[2,1]]]])