# module factorial

def fact(n, acc = 1):
	if n == 1:
		return acc

	return fact(n-1, acc*n)