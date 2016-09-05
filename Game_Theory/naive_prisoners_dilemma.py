import numpy as np

# simulates one round of game
def play(C,D,A,anti_simmetric=False):

	# total population size
	N = C + D

	# probability of picking defector is D/N
	p1 = 1 if np.random.rand() <= D/N else 0
	p2 = 1 if np.random.rand() <= D/N else 0

	# increase population size for players
	if p1 == 0:
		C = C + A[p1][p2]
	else:
		D = D + A[p1][p2]

	if p2 == 0:
		C = C + A[p2][p1]
	else:
		D = D + A[p2][p1]

	# return new distribution
	return C,D,C+D


if __name__=='__main__':
	
	num_simulations = 10
	max_pop_size = 4000000

	# payoff matrix
	prisoners_dilemma = [[2,0],[3,1]]
	battle_of_the_sexes = [[2,3],[3,2]]
	matching_pennies = [[1,-1],[-1,1]]
	
	# run 100 independent simulations w/ same initial conditions
	for i in xrange(num_simulations):
		
		C = 80.
		D = 100. - C
		N = C+D

		# simulate until population hits size
		while N < max_pop_size:
			C,D,N = play(C,D,prisoners_dilemma)

		# print final distribution
		print C/N,D/N