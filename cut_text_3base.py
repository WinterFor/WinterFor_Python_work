#!/user/bin/env python
#cut_text_3base
#import re
#sequence = input('Please Enter the sequence:')
sequence = 'GATGGAACTTGACTACGTAAATTA'
sequence_list = list(sequence)
list_3base = []
if  len(sequence)%3 == 0:
	n = 0
	while n+2<len(sequence):
		base_3 = "".join(sequence_list[n:n+3])
		list_3base.append(base_3)
		n = n+3
	else:
		print("There are the result3:")
else:
	if len(sequence)%3 == 1:
		n = 0
		while n+2<len(sequence)-1:
			base_3 = "".join(sequence_list[n:n+3])
			list_3base.append(base_3)
			n = n+3
		else:
			base_1 = "".join(sequence[-1])
			list_3base.append(base_1)
			print("There are the result1:")
	else:
		n = 0
		while n+2<len(sequence)-2:
			base_3 = "".join(sequence_list[n:n+3])
			list_3base.append(base_3)
			n = n+3
		else:
			base_2 = "".join(sequence[-3:-1])
			list_3base.append(base_2)
			print("There are the result2:")
print(list_3base)