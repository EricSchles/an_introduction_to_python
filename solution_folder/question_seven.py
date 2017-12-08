def formula(x: list, y:list) -> float:
	first_term = [x[i]*y[i] for i in range(len(x))]
	first_term = sum(first_term)
	second_term = 0
	for i in x:
		for j in y:
			second_term += (i - j)
	numerator = first_term + second_term
	denominator = 1
	for i in x:
		denominator *= i
	return numerator / denominator