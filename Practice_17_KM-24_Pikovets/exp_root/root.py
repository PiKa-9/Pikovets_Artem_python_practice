# module root

def root2(x):
	return x ** 0.5

def root3(x):
	if x < 0:
		return - ((abs(x)) ** (1/3))
	else:
		return x ** (1/3)