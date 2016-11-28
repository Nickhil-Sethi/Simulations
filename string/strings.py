def concatenate(a,strings):
	return [a + s for s in strings]

def binary_strings(n):
	if not 0 < n < 9:
		raise ValueError('input must be in (0,9)')
	if n == 0:
		return []
	if n == 1:
		return ['0','1']
	else:
		new = binary_strings(n-1)
		return concatenate('0',new)+concatenate('1',new)

if __name__=='__main__':
	print binary_strings(8)