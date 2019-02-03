# noinspection PyUnusedLocal
def fizz_buzz(number):
	a=number
	isOdd=number%2!=0
	div3=number%3==0
	div5=number%5==0
	in3=str(3) in str(number)
	in5=str(5) in str(number)
	ll=[]
	while a>0:
		ll.append(a%10)
		a=a//10
	sm=len(set(ll)) == 1
	dlx3=(sm) and (number>10)
	dlx= dlx3 and isOdd #this is fake delux
	fx_dlx=dlx and ((div3 or in3) and (div5 or in5))
	if (div3 or in3) and (div5 or in5):
		if dlx:
			return "fizz buzz fake deluxe"
		elif dlx3:
			return "fizz buzz deluxe"
		else:
			return "fizz buzz"
	elif div3 or in3:
		if dlx:
			return "fizz fake deluxe"
		elif dlx3:
			return "fizz deluxe"
		else:
			return "fizz"
	elif div5 or in5:
		if dlx:
			return "buzz fake deluxe"
		elif dlx3:
			return "buzz deluxe"
		else:
			return "buzz"
	elif dlx3:
		if isOdd:
			return "fake deluxe"
		else:
			return "deluxe"
	else:
		return str(number)
