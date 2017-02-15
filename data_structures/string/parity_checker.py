from stack import stack

input = '()()((()()())()())))()))()))'

def parity_checker(my_str):
	if not isinstance(my_str, __builtins__.str):
		raise TypeError('input must be type str')

	my_str = list(my_str)
	s = stack()

	balanced = True
	index = 0

	while index < len(my_str) and balanced:
		
		if my_str[index] == '(':
			s.push('(')
		elif s.is_empty():
			balanced=False
		else:
			s.pop()

		index+=1

	if balanced and s.is_empty():
		return True
	else:
		return False


print parity_checker(input)