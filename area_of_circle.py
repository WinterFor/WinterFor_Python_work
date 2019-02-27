#area of circle
import math

def scircle(x):
	if not isinstance(x ,(int, float)):
		raise TypeError("bad operand type")
	area_of_circle = x*x*math.pi 
	return area_of_circle