# noinspection PyUnusedLocal
def fizz_buzz(number):
    isOdd=number%2!=0
    div3=number%3==0
    div5=number%5==0
    in3=str(3) in str(number)
    in5=str(5) in str(number)
    dlx3=((div3 and in3) or (div5 and in5)) #this my delux
    dlx= dlx3 and isOdd #this is fake delux 
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
    #raise NotImplementedError()
