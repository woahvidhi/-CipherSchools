for i in range(6):
	for j in range(6-i):
		print(" ", end='')
	for k in range(i):
		print("*",end='')
	print('')

c = 65
for i in range(6):
	for j in range(i):
		print(chr(c), end='')
		c+=1
	print('')