#Fibonacci sequence
def Fis(n):
	Fibonacci_sequence_n = []
	if n<3:
		s = 1
		while n>0:
			Fibonacci_sequence_n.append(s)
			n = n-1
		return Fibonacci_sequence_n
	else:
		Fibonacci_sequence_n = [1,1]
		s1 = 1
		s2 = 1
		while n-2>0:
			s3 = s1+s2
			Fibonacci_sequence_n.append(s3)
			s1 = s2
			s2 = s3
			n = n-1
		#return Fibonacci_sequence_n
		return number_n = Fibonacci_sequence_n[n-1]
		return n_sum = sum(Fibonacci_sequence_n)