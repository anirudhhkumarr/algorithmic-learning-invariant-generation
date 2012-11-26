from teacher import rand_mem, EQ

def invjoin(Arr, jointype):
	if Arr!=None:
		ret = Arr[0]
		for i in Arr:
			ret = invariant(jointype, ret, i)
		return ret

def walk(u ,a):
	i = 1
	while i <= m:
		if evaluate(u[b[i]], B) != evaluate(a[b[i]], B):
			u[b[i]] = invariant('not', u[b[i]])
			if rand_mem(u) == True:
				i=0
			else:
				u[b[i]] = invariant('not', u[b[i]])
		i = i + 1
	return u

def MDNF(u):
	if u==None or u==[]:
		return invariant('value', False)
	elif u==False:
		return invariant('value', True)
	else:
		invjoin(u,'and')
	return

def SMT():
	#interface for accessing YICES
	return
	
def evaluate(u, H):
	#have to figure out this
	return
