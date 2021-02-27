import math

def fizz_buzz(n: int) -> str:
	fizz = "fizz" * int(math.cos(n * math.tau / 3))
	buzz = "buzz" * int(math.cos(n * math.tau / 5))
	return (fizz + buzz) or str(n)

for i in range(1, 101):
	print(fizz_buzz(i))