# module logarithm

from math import log as math_log, e as math_e

def log(a, b):
	return math_log(b, a)

def ln(b):
	return math_log(b, math_e)

def lg(b):
	return math_log(b, 10)