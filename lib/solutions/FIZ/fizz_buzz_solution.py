# noinspection PyUnusedLocal
def fizz_buzz(number):
	div3=number%3==0
	div5=number%5==0
	if div3 and div5:
		return "fizz buzz"
	elif div3:
		return "fizz"
	elif div5:
		return "buzz"
	else:
		return str(number)
	raise NotImplementedError()
