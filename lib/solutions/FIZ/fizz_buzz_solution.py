# noinspection PyUnusedLocal
def fizz_buzz(number):
	div3=number%3==0
	div5=number%5==0
	if div3:
		return "fizz"
	elif div5:
		return "buzz"
	elif div5 and div3:
		return "fizz buzz"
	else:
		return str(number)
	raise NotImplementedError()


