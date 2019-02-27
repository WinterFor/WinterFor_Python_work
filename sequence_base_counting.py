#！/user/bin/env python
# count "AT"/"TA"/"GC"/"CG" in a sequence
sequence = input("Please Enter the sequence:")
searching_number = ['AT', 'TA', 'GC', 'CG']
for base in searching_number:
	n = sequence.count(base)
	print('There have ' + str(n) + str(base) +' in the sequence.')