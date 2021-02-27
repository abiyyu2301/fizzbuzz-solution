def fizz_buzz(n: int) -> str:
	hi = max(n,15)
	lo = min(n, 15)

	while hi % lo > 0:
		hi, lo = lo, hi % lo

	return {
		1: str(n),
		3: 'fizz',
		5: 'buzz',
		15: 'fizzbuzz'
	}[lo]

for i in range(1,101):
	print(fizz_buzz(i))