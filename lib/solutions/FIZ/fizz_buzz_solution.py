# noinspection PyUnusedLocal
def fizz_buzz(number):
	a=number
	div3=number%3==0
	div5=number%5==0
	in3=str(3) in str(number)
	in5=str(5) in str(number)
	ll=[]
	while a>0:
		ll.append(a%10)
		a=a//10
	sm=len(set(ll)) == 1
	dlx=(sm) and (number>10)
	fx_dlx=dlx and ((div3 or in3) and (div5 or in5))
	if fx_dlx:
		return "fizz buzz deluxe"
	elif (div3 or in3) and (div5 or in5):
		return "fizz buzz"
	elif div3 or in3:
		if dlx:
			return "fizz deluxe"
		else:
			return "fizz"
	elif div5 or in5:
		if dlx:
			return "buzz deluxe"
		else:
			return "buzz"
	elif dlx:
		return "deluxe"
	else:
		return str(number)
	raise NotImplementedError()




