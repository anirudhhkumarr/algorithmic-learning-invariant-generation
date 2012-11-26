from goto import goto, comefrom, label
from teacher import EQ, rand_mem
from invariant import invariant
from utils import invjoin, walk, evaluate, MDNF
from random import random

under = None
over = None
B = #set of boolean variables
	
def CDNF():
	t = 0
	if EQ(True) == True:
		return True
	else:
		u = EQ(True)
		
	label .zero
	t = t + 1
	(H[t], S[t], a[t]) = (False, None, u)
	
	label .one
	if EQ(invjoin(H, 'and')) == True:
		return invjoin(H, 'and')
	else:
		u = EQ(invjoin(H, 'and'))
	I = []
	for i in range(0, len(H)):
		if evaluate(u, H[i])==False:
			I.append(i)
	if I==[]:
		goto .zero
	mu = []
	for i in I:
		mu.append(walk(u, a[i]))
		S.append(mu[-1] ^ a[i])
	for i in range(0,t):
		H[i] = MDNF(S[i])
	goto .one

def main():
	#{\delta} while \rho do S {\epsilon}
	under = #(\delta OR \epsilon)
	over = #(\epsilon OR \rho)
	inv = None
	while(inv==None):
		inv = CDNF()
	return
	
if __name__ == '__main__':
	main()
