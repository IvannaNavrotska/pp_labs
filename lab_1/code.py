#here you can find gcd of any two integers

def gcd (a,b):

    if type(a) != int or type(b) != int:
        return False
    elif a == 0 and b == 0:
        return
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

#in case you forgot the fibonacci numbers

#in case you forgot the fibonacci numbers

def fibonacci (f):

    if type(f) != int or f < 0:
        return False
    elif f == 0 or f == 1:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)
     
