CYCLE_OF_15 = [
"fizzbuzz", None, None, "fizz",
None, "buzz", "fizz", None,
None, "fizz", "buzz", None,
"fizz", None, None
]


def fizz_buzz(n: int) -> str:
	return CYCLE_OF_15[n % 15] or str(n)

for i in range(1,101):
	print(fizz_buzz(i))