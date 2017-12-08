summation = 0
for i in range(1, 51):
	product = 1
	summation += i
	for j in range(1, 38):
		product *= j
		print(summation, product)