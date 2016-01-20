import numpy as np
import scipy.stats as stats

trump_table = {'a': 5, 'c': 995, 'b': 1, 'd': 999}

def sterling(n):
	return float( np.sqrt(2*np.pi*n)*( (float(n)/np.e)**n) )

def log_sum(u,l=1):
	sum = 0
	for i in xrange(l,u+1):
		sum = sum + np.log(i)
	return sum

def compute_perplexity(table_word):

	a = table_word['a']
	b = table_word['b']
	c = table_word['c']
	d = table_word['d']
	
	l_sum = log_sum(a+b,b+1) + log_sum(c+d,c+1) + log_sum(a+c,a+1) + log_sum(b+d,d+1) - log_sum(a+b+c+d,1)
	return np.e**l_sum
print compute_perplexity(trump_table)
print stats.fisher_exact([[trump_table['a'], trump_table['b']], [trump_table['c'],trump_table['d']]])