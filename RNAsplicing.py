#!/user/bin/env python
#transcription
sequence = input("Please Enter the sequence:")
intron = []
intron_1 = input("Please Enter the intron:")
intron.append(intron_1)
#input_1 = input("Please Enter 1 to continue to add another introns, 0 to break:")
#if (input_1 == "1"):
#	continue
#else:
#	break
#for intron_2 in intron:
#	intron_3 = str(intron_2)
#	sequence = sequence.replace(intron_3, "")
#print(sequence)

input_continue = input("Please Enter 1 to continue to add another introns, 0 to break:")
if input_continue == "1":
	intron_4 = input("Please Enter the intron:")
	intron.append(intron_4)
	input_continue = input("Please Enter 1 to continue to add another introns, 0 to break:")
else:
        pass
for intron_2 in intron:
	intron_3 = str(intron_2)
	sequence = sequence.replace(intron_3, "")
print(sequence)
