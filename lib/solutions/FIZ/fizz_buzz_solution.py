# noinspection PyUnusedLocal
def fizz_buzz(number):
	div3=number%3==0
	div5=number%5==0
	in3=str(3) in str(number)
	in5=str(5) in str(number)
	ll=[]
	while number>0:
		ll.append(number%10)
		number=number//10
	sm=len(set(ll)) == 1
	dlx=(sm) and (number>10)
	if (div3 or in3) and (div5 or in5):
		return "fizz buzz"
	elif div3 or in3:
		return "fizz"
	elif div5 or in5:
		return "buzz"
	else:
		return str(number)
	raise NotImplementedError()

