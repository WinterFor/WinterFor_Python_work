#!/user/bin/env python
#searching a palindromic sequence
sequence = input("Please Enter a sequence:")
minseq = int(input("Please Enter a minimum of the palindromic sequence:"))
maxseq = int(input("Please Enter a maximum of the palindromic sequence:"))
sequence_n = str(len(sequence))
sequence_list = list(sequence)

def tranatcg(sequence):
	sequence_pre_replace = sequence.replace('T', '1')
	sequence_pre_replace = sequence_pre_replace.replace('A', '2')
	sequence_pre_replace = sequence_pre_replace.replace('C', '3')
	sequence_pre_replace = sequence_pre_replace.replace('G', '4')
	sequence_pre_replace = sequence_pre_replace.replace('1', 'A')
	sequence_pre_replace = sequence_pre_replace.replace('2', 'T')
	sequence_pre_replace = sequence_pre_replace.replace('3', 'G')
	sequence_pre_replace = sequence_pre_replace.replace('4', 'C')
	return sequence_pre_replace

sequence_pre_replace = list(tranatcg(sequence))
print(sequence_list)
print(sequence_pre_replace)

#sequence_53 = sequence_list[：：n]
n = int(sequence_n)
for b in range(0,n):
	for c in range(minseq, maxseq+1):
		if b+c<n+1:
			sequence_53 = sequence_list[b:b+c]
			sequence_35 = list(reversed(sequence_pre_replace[b:b+c]))
			if sequence_53 == sequence_35:
				start = str(b+1)
				end = str(b+c+1)
				print('A palindromic sequence ' + 'from ' + start + ' to ' + end + '.')
				sequence_53_str = "".join(sequence_53)
				sequence_35_str = "".join(list(reversed(sequence_35)))
				print(sequence_53_str)
				print(sequence_35_str)
		else:
			continue