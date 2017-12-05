def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

for n in range(100, 1000):
	fib(n)/fib(n-1)