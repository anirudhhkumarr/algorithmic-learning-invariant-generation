from utils import SMT

under = #specify under approximation
over = #specify over approximation
pre = #precondition
post = #postcondition
B = #set of boolean variables

def concretise(u):
	#concretize the boolean formula
	return

def MEM(u):
	theta = concretize(u)
	if SMT(theta) == 'UNSAT':
		return False
	elif SMT(invariant('and', theta, invariant('not', under))) == 'UNSAT':
		return True
	else
		return False
	return ('ABORT', theta)
	
def EQ(u):
	theta = concretise(u)
	if SMT(invariant('and', under, invariant('not', theta))) == 'UNSAT' and invariant('and', theta, invariant('not', over))) == 'UNSAT' and SMT(invariant('and',invariant('and', rho, theta), invariant('not', pre)))=='UNSAT':
		return True
	elif SMT(invariant('and', under, invariant('not', theta))) == 'UNSAT':
		#still have to figure out this
		return
	elif invariant('and', theta, invariant('not', over))) == 'UNSAT':
		#still have to figure out this
		return
	return ('ABORT', theta)

def rand_mem(u):
	if MEM(u) == 'ABORT':
		if random()>0.5:
			return True
		else:
			return False
	else:
		return MEM(u)
