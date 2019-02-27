#ax^2+bx+c=0
import math
import numpy

def quadratic(a, b, c):
	coefficient = [a, b, c]
	for value in coefficient:
		if not isinstance(value, (int, float)):
			raise TypeError("bad operand type")
	delta = b*b-4*a*c
	if delta >= 0:
		sdelta = numpy.sqrt(delta)
		x1 = (-b+sdelta)/(2*a)
		x2 = (-b-sdelta)/(2*a)
		return x1, x2
	else:
		x1 = "no solution! "
		x2 = "no solution! "
		return x1, x2