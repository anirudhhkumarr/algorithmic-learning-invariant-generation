class invariant:
	def __init__(self, deftype, inv, inv2=None):
		self.deftype = deftype
		self.value = None
		self.child = None
		if inv2 == None:
			if deftype == 'value':
				self.value = inv
			else:
				self.child = [inv]
		else:
			self.child = [inv, inv2] 
